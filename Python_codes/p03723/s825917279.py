a, b, c = map(int, input().split())
if a == b == c:
    ans = 0
else:
    ans = 1 << 31
    for x in [a - b, b - c, c - a]:
        if x != 0:
            tmp = 0
            while x % 2 == 0:
                tmp += 1
                x >>= 1
            ans = min(tmp, ans)

if a == b == c and b % 2 == 0:
    print(-1)
else:
    print(ans)