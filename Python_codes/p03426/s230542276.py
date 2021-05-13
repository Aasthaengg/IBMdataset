H, W, D = map(int, input().split())
A_where = [0] * (H*W+1)
A_where[0] = (-1, -1)
for p in range(H):
    A = list(map(int, input().split()))
    for q in range(W):
        A_where[A[q]] = (p, q)

Q = int(input())

DP = [0] * (H*W+1)

for i in range(D+1, H*W+1):
    y1, x1 = A_where[i]
    y2, x2 = A_where[i-D]

    DP[i] = DP[i-D] + abs(y1-y2) + abs(x1-x2)

for i in range(Q):
    l, r = map(int, input().split())
    print(DP[r] - DP[l])
