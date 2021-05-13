import sys, math
from itertools import permutations, combinations
from collections import defaultdict, Counter, deque
from math import factorial#, gcd
from bisect import bisect_left #bisect_left(list, value)
sys.setrecursionlimit(10**7)
enu = enumerate
MOD = 10**9+7
def input(): return sys.stdin.readline()[:-1]
def pri(x): print('\n'.join(map(str, x)))

N, M = map(int, input().split())
C = list(map(int, input().split()))
MAX = 20

dp = [list(range(N+1)) for _ in range(M+1)]

for i in range(1, M+1):
    c = C[i-1]
    for j in range(N+1):
        if j-c>=0:
            dp[i][j] = min(dp[i-1][j-c]+1, dp[i-1][j], dp[i][j-c]+1)
        else:
            dp[i][j] = dp[i-1][j]
#    pri(dp)
print(dp[M][N])

