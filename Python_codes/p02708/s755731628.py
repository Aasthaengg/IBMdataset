n,k=map(int,input().split())
s=0
for i in range(k,n+2):
	#0+...+i-1
	l=i*(i-1)//2
	#n+(n-1)+...+(n-i+1)
	h=(2*n-i+1)*i//2
	s+=h-l+1
print(s%(10**9+7))