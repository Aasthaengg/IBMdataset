N = int(input())

g = [[0] * (10) for _ in range(10)]
for i in range(1, N + 1):
    a = int(str(i)[0])
    b = int(str(i)[-1])
    g[a][b] += 1
ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        ans += g[i][j]*g[j][i]

print(ans)