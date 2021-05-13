mod = 10**9+7
H, W, K = map(int, input().split())

D = [[0]*W for _ in range(W)]
for S in range(1<<W-1):
    if S & S<<1 != 0:
        continue
    #print(bin(S))
    S <<= 1
    for i in range(W):
        if S>>i&1:
            D[i][i-1] += 1
        elif S>>i+1&1:
            D[i][i+1] += 1
        else:
            D[i][i] += 1
    #for d in D:
    #    print(d)

E = [[0]*W for _ in range(W)]
for i in range(W):
    E[i][i] = 1

for i in range(H):
    A = [[0]*W for _ in range(W)]
    for x in range(W):
        for y in range(W):
            A[x][y] = sum(E[x][z] * D[z][y] % mod for z in range(W)) % mod
    E = A

print(A[0][K-1])
