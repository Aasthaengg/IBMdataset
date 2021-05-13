H, W, D = map(int,input().split())
A = []
L = [None for _ in range(H * W)]
for _ in range(H):
    A.append(list(map(int,input().split())))
for i in range(H):
    for j in range(W):
        L[A[i][j]-1] = [i, j]
Q = int(input())
cnt = [[0] for _ in range(D)]
for i in range(D):
    j = i
    while j + D <= H * W - 1:
        cnt[i].append(cnt[i][-1] + abs(L[j + D][0] - L[j][0]) + abs(L[j + D][1] - L[j][1]))
        j += D
for _ in range(Q):
    L, R = map(int,input().split())
    i = (L - 1) % D
    print(cnt[i][(R-1)//D] - cnt[i][(L-1)//D])