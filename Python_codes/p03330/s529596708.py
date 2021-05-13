from collections import defaultdict
from itertools import permutations

N, C = map(int,input().split())
D = []
for _ in range(C):
    D.append(list(map(int,input().split())))
c = []
for _ in range(N):
    c.append(list(map(int,input().split())))

P = [defaultdict(int) for _ in range(3)]
for i in range(N):
    for j in range(N):
        P[(i+j)%3][c[i][j]-1] += 1

ans = float('inf')
for L in permutations([i for i in range(C)], 3):
    cnt = 0
    for i in range(3):
        for j in range(C):
            cnt += P[i][j] * D[j][L[i]]
    ans = min(ans, cnt)

print(ans)