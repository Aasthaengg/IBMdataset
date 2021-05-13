import sys
from itertools import permutations
n, c = [int(i) for i in sys.stdin.readline().split()]
D = dict()
C = dict()
MOD_dict = {i : [0 for j in range(30)] for i in range(3)}
INF = 10 ** 18
for i in range(c):
    inp = [int(i) for i in sys.stdin.readline().split()]
    D[i] = inp
for i in range(n):
    inp = [int(i) - 1 for i in sys.stdin.readline().split()]
    C[i] = inp
    for j, k in enumerate(inp):
        MOD_dict[(i+j) % 3][k] += 1
best = INF
for perm in permutations(range(c), 3):
    cost = 0
    for i in range(c):
        cost += MOD_dict[0][i] * D[i][perm[0]] +  MOD_dict[1][i] * D[i][perm[1]] + \
                MOD_dict[2][i] * D[i][perm[2]]
    best = min(cost, best)
print(best)