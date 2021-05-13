from itertools import permutations
import sys
input = sys.stdin.readline
N, M, R = map(int, input().split())
r = [int(i)-1 for i in input().split()]
D = [[float("inf")] * N for _ in range(N)]
for a, b, c in [[int(i) for i in input().split()] for _ in range(M)]:
    a -= 1
    b -= 1
    D[a][b] = c
    D[b][a] = c
for i in range(N):
    D[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            D[i][j] = min(D[i][j], D[i][k] + D[k][j])

ans = float("inf")
for l in permutations(range(R)):
    l = list(l)
    c = 0
    for i in range(R - 1):
        c += D[r[l[i]]][r[l[i + 1]]]
    ans = min(ans, c)
print(ans)