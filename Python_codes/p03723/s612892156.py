a, b, c = map(int, input().split())
ans = 0

if a % 2 == 0 and b % 2 == 0 and c % 2 == 0 and a == b == c:
    print(-1)
else :
    while a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
        aa, bb, cc = a, b, c
        a = bb // 2 + cc // 2
        b = aa // 2 + cc // 2
        c = aa // 2 + bb // 2
        ans += 1
    print(ans)

