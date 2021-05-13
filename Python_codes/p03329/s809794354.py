import sys, math
from itertools import permutations, combinations
from collections import defaultdict, Counter, deque
from math import factorial
from bisect import bisect_left #bisect_left(list, value)
#from fractions import gcd
sys.setrecursionlimit(10**7)
enu = enumerate
MOD = 10**9+7
def input(): return sys.stdin.readline()[:-1]
def pri(x): print('\n'.join(map(str, x)))

N = int(input())
INF = 10**18

res = 0
dp = [INF]*(10*N)
dp[0] = 0
for i in range(0, N):
    dp[i+1] = min(dp[i+1], dp[i]+1)

    j = 1
    while i+6**j <= N:
        dp[i+6**j] = min(dp[i+6**j], dp[i]+1)
        j += 1

    l = 1
    while i+9**l <= N:
        dp[i+9**l] = min(dp[i+9**l], dp[i]+1)
        l += 1

print(dp[N])


