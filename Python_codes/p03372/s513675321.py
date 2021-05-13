N, C = map(int, input().split())
X = []
for _ in range(N):
    x, v = map(int, input().split())
    X.append((v, x))

A = [0] * (N+1)
B = [0] * (N+1)
MAA = [0] * (N+1)
MAB = [0] * (N+1)

for i in range(N):
    A[i+1] = A[i] + X[i][0] - (X[i][1] - (X[i-1][1] if i else 0))
    MAA[i+1] = max(MAA[i], A[i+1])

for i in range(N)[::-1]:
    B[i] = B[i+1] + X[i][0] + (X[i][1] - (X[i+1][1] if i < N-1 else C))
    MAB[i] = max(MAB[i+1], B[i])

ma = max(max(MAA), max(MAB))
for i in range(N):
    ma = max(ma, A[i+1] + MAB[i+1] - X[i][1])
    ma = max(ma, B[i] + MAA[i] + X[i][1] - C)

print(ma)