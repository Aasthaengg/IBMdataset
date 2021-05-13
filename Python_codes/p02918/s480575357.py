import sys, math
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mod = 10**9 + 7

N, K = rl()
S = rs()

import itertools
g = list(itertools.groupby(S))

print(N-max(len(g)-1-2*K, 0)-1)
