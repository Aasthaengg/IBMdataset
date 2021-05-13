a, b, c = map(int,input().split())
k = 1
ans = 0

for i in range(40):
    if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
        d = a // 2
        e = b // 2
        f = c // 2
        a = e + f
        b = d + f
        c = d + e
        ans += 1
    else:
        k = 0
        break

if k == 1:
    print(-1)
else:
    print(ans)