n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if a[i][j] > a[i][k]+a[k][j]:
                print(-1)
                exit(0)

ans = 0
for i in range(n):
    for j in range(i+1, n):
        ok = True
        for k in range(n):
            if i == k or j == k:
                continue
            if a[i][j] == a[i][k]+a[k][j]:
                ok = False
                break
        if ok:
            ans += a[i][j]
print(ans)
