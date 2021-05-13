import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
#mod = 998244353
INF = 10**18
eps = 10**-7

N = int(readline())
D = list(map(int,readline().split()))
M = int(readline())
T = list(map(int,readline().split()))

from collections import defaultdict
d_dict = defaultdict(int)
for t in T:
    d_dict[t] += 1
for d in D:
    if d_dict[d] > 0:
        d_dict[d] -= 1

print('YES' if sum(v for v in d_dict.values()) == 0 else 'NO')
