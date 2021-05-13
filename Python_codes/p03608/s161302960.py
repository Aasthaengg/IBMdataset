import sys
input = sys.stdin.readline

from itertools import permutations


n, m, r = map(int, input().split())
R = list(map(int, input().split()))

D = [[float("inf")] * (n + 1) for _ in range(n + 1)]
for i in range(n + 1):
    D[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    D[a][b] = c; D[b][a] = c

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            D[i][j] = min(D[i][j], D[i][k] + D[k][j])

P = list(permutations(R))

answer = float("inf")
for p in P:
    temporary = 0
    for k in range(r - 1):
        i, j = p[k], p[k + 1]
        temporary += D[i][j]
    answer = min(answer, temporary)

print(answer)
