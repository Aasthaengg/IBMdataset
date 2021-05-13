def popcnt(n):
    c = (n & 0x5555555555555555) + ((n >> 1) & 0x5555555555555555)
    c = (c & 0x3333333333333333) + ((c >> 2) & 0x3333333333333333)
    c = (c & 0x0f0f0f0f0f0f0f0f) + ((c >> 4) & 0x0f0f0f0f0f0f0f0f)
    c = (c & 0x00ff00ff00ff00ff) + ((c >> 8) & 0x00ff00ff00ff00ff)
    c = (c & 0x0000ffff0000ffff) + ((c >> 16) & 0x0000ffff0000ffff)
    c = (c & 0x00000000ffffffff) + ((c >> 32) & 0x00000000ffffffff)
    return c


n = int(input())
f = [sum([(1 << (9 - x)) * y for x, y in enumerate(list(map(int, input().split())))]) for _ in range(n)]
p = [list(map(int, input().split())) for _ in range(n)]

ans = -1 << 60
for i in range(1, 1024):
    tmp = 0
    for x, y in zip(f, p):
        tmp += y[popcnt(i & x)]
    ans = max(ans, tmp)

print(ans)