N, M = map(int, input().split())
W = [list(map(int, input().split())) for _ in range(M)]
W.sort()
C = [0 for i in range(N-1)]
r = W[0][1]-1
for i in range(1, M):
    r = min(W[i][1]-1, r)
    if r <= W[i][0]-1:
        C[W[i-1][0]-1] = 1
        r = W[i][1]-1
C[W[-1][0]-1] = 1
print(sum(C))