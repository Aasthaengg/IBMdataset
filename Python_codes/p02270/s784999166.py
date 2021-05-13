import sys
n, k = map(int, input().split())
T = [int(input()) for i in range(n)]
def c(mid):
	global k,T,n
	i=0
	for j in range(k):
		s=0
		while s+T[i]<=mid:
			s+=T[i]
			i+=1
			if(i == n):
				return n
	return i
def Allocation():
	l=0
	r=sys.maxsize
	while r-l>1:
		mid=(l+r)//2
		v=c(mid)
		if (v>=n):
			r=mid
		else:
			l=mid
	return r
x=Allocation()
print(x)

