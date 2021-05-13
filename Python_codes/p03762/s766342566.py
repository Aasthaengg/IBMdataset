import sys
input = sys.stdin.readline
mod=10**9+7
n,m=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
xsum=0
for i in range(n):
    xsum+=x[-i-1]*(n-2*i-1)%mod
ysum=0
for i in range(m):
    ysum+=y[-i-1]*(m-2*i-1)%mod

print(xsum*ysum%mod)
