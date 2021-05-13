import itertools
from collections import defaultdict
from sys import exit

N = int(input())
balls = sorted([tuple(map(int, input().split())) for _ in range(N)])

if N == 1:
    print(1)
    exit()

d = defaultdict(int)
for i, j in itertools.combinations(range(N), 2):
    d[(balls[j][0] - balls[i][0], balls[j][1] - balls[i][1])] += 1
print(N - max(d.values()))
