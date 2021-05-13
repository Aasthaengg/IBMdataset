N, C = map(int, input().split())
X, V, D, E = [0], [0], [0], [0] * (N + 2)
for i in range(1, N + 1):
    x, v = map(int, input().split())
    X.append(x)
    V.append(v + V[i - 1])
    D.append(max(D[i - 1], V[i] - X[i]))

for i in range(N, 0, -1):
    E[i] = max(E[i + 1], (V[N] - V[i - 1]) - (C - X[i]))

ret = max(D[N], E[1])
for i in range(1, N + 1):
    ret = max(ret, D[i] + E[i + 1] - X[i])
for i in range(N, 0, -1):
    ret = max(ret, E[i] + D[i - 1] - (C - X[i]))
print(ret)
