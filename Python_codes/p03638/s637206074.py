H, W = list(map(int, input().split()))
N = int(input())
A = list(map(int, input().split()))

B = []

for i, a in enumerate(A):
    for _ in range(a):
        B.append(i+1)

M = []
for _ in range(H):
    M.append([0] * W)

for h in range(H):
    for w in range(W):
        if h % 2 == 0:
            M[h][w] = B[w + h*W]
        else:
            M[h][W-w-1] = B[w + h*W]

    print(*M[h])
