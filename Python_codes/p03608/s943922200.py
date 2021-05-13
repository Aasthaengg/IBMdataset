import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7

from itertools import permutations

N, M, r = map(int, input().split())
R = list(map(int, input().split()))

INF = 10 ** 9

G = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(N + 1):
    G[i][i] = 0

for _ in range(M):
    A, B, C = map(int, input().split())
    G[A][B] = C
    G[B][A] = C

for k in range(N + 1):
    for i in range(N + 1):
        for j in range(N + 1):
            G[i][j] = min(G[i][j], G[i][k] + G[k][j])

ans = INF
for tmp in permutations(R):
    score = 0
    for i in range(r - 1):
        score += G[tmp[i]][tmp[i + 1]]
    ans = min(ans, score)

print (ans)
