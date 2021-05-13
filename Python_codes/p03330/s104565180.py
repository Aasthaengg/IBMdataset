N, C = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(C)]
c = [list(map(int, input().split())) for _ in range(N)]
sum_val = [[0] * C for _ in range(3)]

for color in range(1, C + 1):
    for i in range(N):
        for j in range(N):
            sum_val[(i + j) % 3][color - 1] += D[c[i][j] - 1][color - 1]

ans = float('inf')
for i in range(C):
    for j in range(C):
        for k in range(C):
            if i == j or j == k or i == k:
                continue
            ans = min(ans, sum_val[0][i] + sum_val[1][j] + sum_val[2][k])
print(ans)