K=int(input())
s=input().split(' ')
a=[int(s[i]) for i in range(len(s))]
n=len(s)

def solve():
	x,y=2,2
	for i in range(n-1,-1,-1):
		u=(x+a[i]-1)//a[i]
		v=y//a[i]
		if (a[i]*v<x): return -1,-1
		x=a[i]*u
		y=a[i]*(v+1)-1
	return x,y

x,y=solve()
if (x==-1): print(-1)
else: print('%d %d'%(x,y))