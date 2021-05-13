n, m = map(int,input().split())

a = []
for i in range(n):
    a.append(list(map(int,input().split())))

ans = 1000000000000000
for i in range(2 ** n):
    check = 0
    ac = 0
    tmp = 0
    for j in range(n):
        if (i >> j) & 1:
            check += a[j][0] * 100 * (j + 1) + a[j][1]
            tmp += a[j][0]
        
        if check >= m:
            ans = min(ans, tmp)

        else:
            for k in reversed(range(n)):
                if not (i >> k) & 1:
                    ac = -(-(m - check) // ((k + 1) * 100))
                    if ac < a[k][0]:
                        ans = min(ans, ac + tmp)

print(ans)