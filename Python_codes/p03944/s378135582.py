W, H, N = map(int,input().split())
x = 0
y = 0
a = 0
X = []
Y = []
A = []
for i in range(N):
    x, y, a = map(int,input().split())
    X.append(x)
    Y.append(y)
    A.append(a)
P = [[0 for i in range(W)] for j in range(H)]
for i in range(N):
    if A[i] == 1:
        for j in range(X[i]):
            for k in range(H):
                P[k][j] = 1
    elif A[i] == 2:
        for j in range(X[i],W):
            for k in range(H):
                P[k][j] = 1
    elif A[i] == 3:
        for j in range(Y[i]):
            for k in range(W):
                P[j][k] = 1
    elif A[i] == 4:
        for j in range(Y[i],H):
            for k in range(W):
                P[j][k] = 1
ans = 0
for i in range(W):
    for j in range(H):
        if P[j][i] == 0:
            ans += 1
print(ans)
