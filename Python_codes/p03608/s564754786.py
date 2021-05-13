N, M, R = map(int, input().split())
*r, = map(lambda x:int(x)-1, input().split())
D = [[float('inf')]*N for _ in range(N)]
for i in range(N): D[i][i] = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    D[a-1][b-1] = c
    D[b-1][a-1] = c

for k in range(N):
    for i in range(N):
        for j in range(N):
            D[i][j] = min(D[i][j], D[i][k] + D[k][j])

import itertools
ans = float('inf')
for s in itertools.permutations(r, R):
    tot = [D[s[i]][s[i+1]] for i in range(R-1)]
    tot = sum(tot)
    ans = min(ans, tot)

print(ans)