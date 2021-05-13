import sys
input = sys.stdin.readline
from collections import defaultdict

n, d = int(input()), defaultdict(int)
s = list(map(int, input().split()))
for i in s: d[i] += 1
for i in range(1, n + 1): print(d[i])