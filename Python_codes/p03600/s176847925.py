n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
b = [[1]*n for i in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if a[i][k] + a[k][j] < a[i][j]:
                print(-1)
                exit()
            elif a[i][k] + a[k][j] == a[i][j] and i!=k!=j:
                b[i][j] = 0

ans = 0
for i in range(n):
    for j in range(n):
        if b[i][j]:
            ans += a[i][j]
print(ans//2)