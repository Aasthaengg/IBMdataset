n = int(input())
a = [[int(i) for i in input().split()] for _ in range(n)]
ans = 0
b = [i[:] for i in a[:]]

for k in range(n):
    for i in range(n):
        for j in range(n):
            b[i][j] = min(b[i][j],b[i][k]+b[k][j])

flag = False
for i in range(n):
    for j in range(n):
        if b[i][j] < a[i][j]:
            ans = -1
            flag = True
            break
        if b[i][j] == a[i][j]:
            for k in range(n):
                if k == i or k == j: continue
                if b[i][j] == b[i][k] + b[k][j]: break
            else:
                ans += b[i][j]
    if flag: break

ans //= 2
print(ans)