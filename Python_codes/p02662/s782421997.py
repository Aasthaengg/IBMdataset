#from collections import deque,defaultdict
from sys import stdin
input = stdin.readline
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**18
R = 998244353

def ddprint(x):
  if DBG:
    print(x)

hf = pow(2,R-2,R)
n,s = inm()
a = inl()
dp = [[0]*(s+1) for i in range(n+1)]
for i in range(n+1):
    dp[i][0] = pow(2,n,R)
sm = 0
for i in range(1,n+1):
    dp[i] = [x for x in dp[i-1]]
    for j in range(s):
        if dp[i-1][j]>0 and j+a[i-1]<=s:
            dp[i][j+a[i-1]] = (dp[i][j+a[i-1]]+dp[i-1][j]*hf)%R
    #ddprint(i)
    #ddprint(dp[i])
print(dp[n][s])
