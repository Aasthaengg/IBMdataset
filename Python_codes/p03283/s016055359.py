from itertools import accumulate

N, M, Q = map(int, input().split())
DP = [[0] * N for _ in range(N)]
for _ in range(M):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    DP[l][r] += 1
Query = [tuple(map(int, input().split()))for _ in range(Q)]
for w in range(1, N):
    for i in range(N):
        j = i + w
        if j >= N:
            break
        DP[i][j] += DP[i][j-1]
        DP[i][j] += DP[i+1][j]
        DP[i][j] -= DP[i+1][j-1]
for p, q in Query:
    print(DP[p-1][q-1])

