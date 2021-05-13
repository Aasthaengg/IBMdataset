N, M = map(int, input().split())
D = [[0 if i == j else 1<<100 for j in range(N)] for i in range(N)]
X = []
for _ in range(M):
    a, b, c = map(int, input().split())
    X.append([a-1, b-1, c])
    D[a-1][b-1] = c
    D[b-1][a-1] = c

for k in range(N):
    for i in range(N):
        for j in range(N):
            D[i][j] = min(D[i][j], D[i][k] + D[k][j])

print(sum([1 if D[a][b] < c else 0 for a, b, c in X]))