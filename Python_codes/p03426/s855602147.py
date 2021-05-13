H, W, D = map(int,input().split())
data = [0] * (H * W + D + 1)
for i in range(H):
    A = list(map(int,input().split()))
    for j in range(W):
        data[A[j] + D] = [i, j]
Q = int(input())
S = [0] * (H * W + D + 1)
for i in range(H * W):
    if i >= D:
        S[i + D + 1] = S[i + 1] + abs(data[i + D + 1][0] - data[i + 1][0]) + abs(data[i + D + 1][1] - data[i + 1][1])
for i in range(Q):
    L, R = map(int,input().split())
    print(S[R + D] - S[L + D])