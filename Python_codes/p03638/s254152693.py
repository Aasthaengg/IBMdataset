H, W = map(int, input().split())
N = int(input())
A = [int(a) for a in input().split()]
X = [[-1] * W for _ in range(H)]
k = 0
c = 0
for i in range(H):
    for j in range(W)[::(-1 if i&1 else 1)]:
        X[i][j] = k+1
        c += 1
        if c >= A[k] and k < N-1:
            k += 1
            c = 0
for x in X:
    print(*x)