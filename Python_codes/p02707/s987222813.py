import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input().strip())
dp = [0] * (n+1)
A = [int(i) for i in input().strip().split()]

for a in A:
    dp[a] += 1

for i in range(1, n + 1):
    print(dp[i])