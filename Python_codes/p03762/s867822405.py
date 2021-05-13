import sys
input=sys.stdin.buffer.readline
mod=10**9+7

n,m=map(int,input().split())
*x,=map(int,input().split())
*y,=map(int,input().split())
xd=[i-j for j,i in zip(x,x[1:])]
yd=[i-j for j,i in zip(y,y[1:])]
xs=ys=0
for i,d in enumerate(xd):
	xs+=d*(i+1)*(n-1-i)%mod
	xs%=mod
for i,d in enumerate(yd):
	ys+=d*(i+1)*(m-1-i)%mod
	ys%=mod
print(xs*ys%mod)