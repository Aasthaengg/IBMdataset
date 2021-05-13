from sys import stdin
from collections import defaultdict
inp = lambda : stdin.readline().strip()

t = int(inp())
d = {"AC":0,"WA":0,"TLE":0,"RE":0}
for _ in range(t):
    d[inp()] += 1

for i, j in d.items():
    print(i, 'x', j)