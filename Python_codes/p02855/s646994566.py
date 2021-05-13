H, W, K = [int(_) for _ in input().split()]

S = [input() for _ in range(H)]

k = 0
A = [[0 for _ in range(W)] for _ in range(H)]

for i, L in enumerate(S):
    f = 1
    for j, a in enumerate(L):
        if a == "#":
            k += 1
            f = 0
        A[i][j] = k + f

for i in range(1, H):
    if S[i].count("#") == 0:
        for j in range(W):
            A[i][j] = A[i-1][j]

for i in range(H-1)[::-1]:
    if S[i].count("#") == 0:
        for j in range(W):
            A[i][j] = A[i+1][j]

for l in A:
    print(" ".join([str(a) for a in l]))
