#dt = {} for i in x: dt[i] = dt.get(i,0)+1
import sys;input = sys.stdin.readline
inp,ip = lambda :int(input()),lambda :[int(w) for w in input().split()]

n = inp()
dp = [[0]*3 for i in range(n)]
a,b,c = [],[],[]
for _ in range(n):
    aa,bb,cc = ip()
    a.append(aa)
    b.append(bb)
    c.append(cc)
dp[0] = [a[0],b[0],c[0]]
for i in range(1,n):
    dp[i][0] = a[i] + max(dp[i-1][1],dp[i-1][2])
    dp[i][1] = b[i] + max(dp[i-1][0],dp[i-1][2])
    dp[i][2] = c[i] + max(dp[i-1][0],dp[i-1][1])
print(max(dp[-1]))
