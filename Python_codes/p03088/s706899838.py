N = int(input())

C = 10**9+7
n = 5
num = max(N+1, 6)
L = [0 for i in range(num)]
X = [0 for i in range(num)]
Y = [0 for i in range(num)]
Z = [0 for i in range(num)]
W = [0 for i in range(num)]
G = [0 for i in range(num)]
L[3] = 61
L[4] = 230
X[3] = 3
X[4] = 12
Y[3] = 4
Y[4] = 16
Z[3] = 4
Z[4] = 15
W[3] = 3
W[4] = 12
W[5] = 48
G[3] = 15
G[4] = 58
while n <= N:
    L[n] = 4*L[n-1] - (X[n-1]+Y[n-1]+Z[n-1]+W[n-1])
    G[n] = L[n-1]-X[n-1]
    X[n] = L[n-2]-G[n-2]
    Y[n] = L[n-2]
    Z[n] = L[n-2]-X[n-2]
    if n > 5:
        W[n] = L[n-3]*3
    n += 1

print(L[N]%C)