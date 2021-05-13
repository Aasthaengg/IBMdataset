import sys
readline = sys.stdin.readline
N, M, Q = map(int, readline().split())
X = [[0] * N for _ in range(N)]
for _ in range(M):
    l, r = map(int, readline().split())
    X[l-1][r-1] += 1

S = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(N):
    for j in range(N):
        S[i+1][j+1] = S[i+1][j] + X[i][j]

for _ in range(Q):
    p, q = map(int, readline().split())
    p -= 1
    q -= 1
    ans = sum(S[i][q+1] - S[i][p] for i in range(p + 1, q + 2))
    print(ans)