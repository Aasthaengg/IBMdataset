N, M = map(int, input().split())
a = []
for i in range(N):
    a += [list(map(int, input().split()))]
a.sort(key=lambda x: x[0])
i, ans = 0, 0
while M != 0 or i < N:
    if M > a[i][1]:
        M -= a[i][1]
        ans += a[i][0]*a[i][1]
    else:
        ans += a[i][0]*M
        M = 0
        break
    i += 1
print(ans)
