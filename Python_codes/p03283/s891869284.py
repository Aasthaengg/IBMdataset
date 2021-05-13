import sys
input = sys.stdin.readline

N, M, Q = map(int, input().split())
cum = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    l, r = map(int, input().split())
    cum[l][r] += 1
for i in range(1, N+1):
    for j in range(i+1, N+1):
        cum[i][j] += cum[i][j-1]
ans = []
for _ in range(Q):
    p, q = map(int, input().split())
    tot = 0
    for i in range(p, q+1):
        tot += cum[i][q]
    ans.append(tot)
print(*ans, sep="\n")
