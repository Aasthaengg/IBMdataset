import sys
from itertools import permutations
N, C = map(int, sys.stdin.readline().rstrip().split())

d = []
for _ in range(C):
    d.append(tuple(map(int, sys.stdin.readline().rstrip().split())))

r_0 = []
r_1 = []
r_2 = []
for i in range(N):
    g = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(N):
        if (i + j) % 3 == 0:
            r_0.append(g[j])
        elif (i + j) % 3 == 1:
            r_1.append(g[j])
        else:
            r_2.append(g[j])

def get_cost(r):
    cost = [0] * (C + 1)
    for c in range(1, C + 1):
        for i in r:
            cost[c] += d[i - 1][c - 1]

    return cost

cost_0 = get_cost(r_0)
cost_1 = get_cost(r_1)
cost_2 = get_cost(r_2)

ans = 10**18
for c_0, c_1, c_2 in permutations(range(1, C + 1), 3):
    total = cost_0[c_0] + cost_1[c_1] + cost_2[c_2]
    ans = min(ans, total)
print(ans)