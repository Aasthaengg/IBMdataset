import itertools
N, C = map(int, input().split())
D = [[int(a) for a in input().split()] for i in range(C)]
X = [[int(a)-1 for a in input().split()] for i in range(N)]
T = [[0] * C for _ in range(3)]
for i in range(N):
    for j in range(N):
        T[(i+j)%3][X[i][j]] += 1

P = [[0] * C for _ in range(3)]
for i in range(3):
    for j in range(C):
        P[i][j] = sum([D[k][j] * T[i][k] for k in range(C)])
    
ans = 1<<100
for a, b, c in itertools.permutations(range(C), 3):
    ans = min(ans, P[0][a] + P[1][b] + P[2][c])
print(ans)