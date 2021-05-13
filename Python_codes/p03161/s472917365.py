#dt = {} for i in x: dt[i] = dt.get(i,0)+1
import sys;input = sys.stdin.readline
inp,ip = lambda :int(input()),lambda :[int(w) for w in input().split()]

n,k = ip()
x = ip()
dp = [0]*n
for i in range(1,n):
    mn = float('inf')
    for j in range(max(0,i-k),i):
        mn = min(mn,dp[j]+abs(x[j]-x[i]))
    dp[i] = mn
    #print(dp)
print(dp[-1])
