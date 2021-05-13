import sys
sys.setrecursionlimit(10000000)
def input():
    return sys.stdin.readline()[:-1]
from collections import *
import math
from bisect import *
INF = float('inf')

N, K = map(int, input().split())
a = list(map(int, input().split()))
dp = [0] * (K+1)
for i in range(K+1):
    for j in range(N):
        if a[j] <= i:
            dp[i] |= dp[i-a[j]] == 0
ans = 'First' if dp[K] else 'Second'
print(ans)
