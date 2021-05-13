def max2(x,y):
    return x if x > y else y

def popcnt(n):
    c = (n & 0x5555555555555555) + ((n>>1) & 0x5555555555555555)
    c = (c & 0x3333333333333333) + ((c>>2) & 0x3333333333333333)
    c = (c & 0x0f0f0f0f0f0f0f0f) + ((c>>4) & 0x0f0f0f0f0f0f0f0f)
    c = (c & 0x00ff00ff00ff00ff) + ((c>>8) & 0x00ff00ff00ff00ff)
    c = (c & 0x0000ffff0000ffff) + ((c>>16) & 0x0000ffff0000ffff)
    c = (c & 0x00000000ffffffff) + ((c>>32) & 0x00000000ffffffff)
    return c

N = int(input())
data = [[] for _ in range(N)]
res = 0
for i in range(N):
    for _ in range(int(input())):
        data[i].append(tuple(map(int, input().split())))
for n in range(1 << N):
    flg = False
    for i in range(N):
        for x, y in data[i]:
            x -= 1
            if (n>>i)&1 == 1:
                if (n>>x)&1 != y:
                    flg = True
                    break
        if flg:
            break
        if i == N-1:
            res = max2(res, popcnt(n))
print(res)
