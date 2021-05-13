ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
ips = lambda:input().split()
import collections
import math
import itertools
import heapq as hq

n,m = ma()
s = ips()
t = ips()
dp = [[0]*(m+1) for i in range(n+1) ] # dp[i][j]は s[i],t[j]まで見た時初めて一致する整数列の個数 0idx
tot = [[0]*(m+1) for i in range(n+1) ] #tot[n][m] n,mまで見た時に一致するもの全部, sum dp[0:i+1][0:j+1]
mod=10**9+7
for i in range(n):
    for j in range(m):
        if s[i]==t[j]:
            dp[i][j]=tot[i-1][j-1]+1
        else:
            dp[i][j]=0
        tot[i][j] = (dp[i][j] + tot[i][j-1]+tot[i-1][j] -tot[i-1][j-1])%mod

print((tot[n-1][m-1]+1)%mod)
#print(tot)
#print(dp)
