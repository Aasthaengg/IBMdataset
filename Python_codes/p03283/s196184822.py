N, M, Q = map(int, input().split())
LR = [[0 for j in range(N+1)] for i in range(N+1)]
for m in range(M):
    l, r = map(int, input().split())
    LR[l][r] += 1
# cumsum R
for i in range(N+1):
    for j in range(1, N+1):
        LR[i][j] += LR[i][j-1]
# cunsun L
for i in range(N-1, -1, -1):
    for j in range(N+1):
        LR[i][j] += LR[i+1][j]

for i in range(Q):
    p, q = map(int, input().split())
    print(LR[p][q])
