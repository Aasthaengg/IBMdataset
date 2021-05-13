N, W = map(int, input().split())
w0, v0 = map(int, input().split())
X = [[] for _ in range(4)]
X[0].append(v0)
for _ in range(N-1):
    w, v = map(int, input().split())
    X[w-w0].append(v)

X = [[0] + sorted(x)[::-1] for x in X]
for i in range(4):
    for j in range(1, len(X[i])):
        X[i][j] += X[i][j-1]
ma = 0
for i in range(N+1):
    for j in range(N+1-i):
        for k in range(N+1-i-j):
            l = min(N-i-j-k, (W - (w0 * i + (w0+1) * j + (w0+2) * k)) // (w0+3))
            if l < 0: continue
            if i < len(X[0]) and j < len(X[1]) and k < len(X[2]) and l < len(X[3]):
                ma = max(ma, X[0][i] + X[1][j] + X[2][k] + X[3][l])
print(ma)