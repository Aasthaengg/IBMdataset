# sys.stdin.readline()
import sys
input = sys.stdin.readline

N,K=map(int, input().split())
h=list(map(int, input().split()))
import numpy as np 
      
f_inf = float('inf')
dp = [f_inf]*N
dp[0]=0
# hの配列を作る。
h = np.array(h)
 
#配るDP
for i in range(1,N):
    # start は負になることはない。
    start = max(0, i-K)
    # 行列として足し算できるのでforを使う必要がない。
    dp[i] = min(dp[start: i] + np.abs(h[i] - h[start: i]))
    
print(dp[-1])