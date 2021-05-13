from itertools import permutations
import sys
input = sys.stdin.readline
N, C = map(int, input().split())

D = [tuple(map(int, input().split())) for _ in [0]*C]
K = [tuple(map(int, input().split())) for _ in [0]*N]

T = [[0]*C for _ in [0]*3]

for i, _k in enumerate(K):
    for j, k in enumerate(_k):
        z = (i+j) % 3
        T[z][k-1] += 1

ans = float('inf')
for a, b, c in permutations(range(C), 3):
    cost = 0
    cost += sum(t*D[i][a] for i, t in enumerate(T[0]))
    cost += sum(t*D[i][b] for i, t in enumerate(T[1]))
    cost += sum(t*D[i][c] for i, t in enumerate(T[2]))
    ans = min(ans, cost)
print(ans)
