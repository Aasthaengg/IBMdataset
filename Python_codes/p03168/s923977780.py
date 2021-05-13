from collections import Counter
from collections import deque
import math
import bisect
import sys
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

n=int(input())
p=list(map(float,input().split()))
dp=[[0]*(n+1) for i in range(n+1)]
dp[0][0]=1
for i in range(n):
    for k in range(n):
        dp[i+1][k]+=dp[i][k]*(1-p[i])
        dp[i+1][k+1]+=dp[i][k]*p[i]
print(sum(dp[n][n//2+1:]))