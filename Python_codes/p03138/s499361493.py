import sys
import math
import bisect
def input():
    return sys.stdin.readline()[:-1]
n,k = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
keta = 0
lis = []

tt = k
num=0
while tt!=0:
    tt//=2
    num+=1

if k==0:
    num=1
num=48
for _ in range(num):
    tmp = 0
    for i in range(n):
        if a[i]%2==0:
            tmp+=1
        a[i]//=2
    lis.append([tmp,n-tmp])
    keta+=1
dp = [[0 for i in range(2)]for i in range(num+1)]
dp[0][0]=0
for i in range(1,num+1):
    jum = k>>(num-i)&1
    dp[i][0] += dp[i-1][0]+lis[num-i][1-jum]*2**(num-i)
    if dp[i-1][1] and jum==0:
        dp[i][1] += dp[i-1][1]+max(lis[num-i])*2**(num-i)
    elif dp[i-1][1] and jum==1:
        dp[i][1] += max(dp[i-1][1]+max(lis[num-i])*2**(num-i),dp[i-1][0]+lis[num-i][jum]*2**(num-i))
    elif dp[i-1][1]==0 and jum==1:
        dp[i][1] += dp[i-1][0]+lis[num-i][jum]*2**(num-i)

print(max(dp[-1]))
