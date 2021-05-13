import sys
from collections import defaultdict
input = sys.stdin.readline
N = int(input())
A = [int(x) for x in input().strip().split()]
d = defaultdict(int)
for a in A:
    d[a] += 1
l = [(x - 1) % 2 for x in d.values() if x > 1 and x % 2 == 0]
print(len(d) - len(l) % 2)