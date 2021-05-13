from itertools import permutations
INF = 10 ** 8
N, M, R = map(int,input().split())
r = list(map(lambda x: int(x)-1 ,input().split()))
MAP = [[INF for i in range(N)] for j in range(N)]
for i in range(M):
    A, B, C = map(int,input().split())
    MAP[A-1][B-1] = C
    MAP[B-1][A-1] = C
for k in range(N):
    for i in range(N):
        for j in range(N):
            MAP[i][j] = min(MAP[i][j], MAP[i][k] + MAP[k][j])

ans = INF
for L in permutations(r):
    temp = 0
    for i in range(R-1):
        temp += MAP[L[i]][L[i+1]]
    ans = min(ans, temp)
print(ans)