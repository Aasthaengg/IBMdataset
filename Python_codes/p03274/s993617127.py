n,k=map(int,input().split())
x=list(map(int,input().split()))


res=3*10**8+1

for i in range(n-k+1):
	l=x[i]
	r=x[i+k-1]
	if l*r>=0:
		res=min(res,max(abs(l),abs(r)))
	else:
		res=min(res,abs(l)+abs(r)+min(abs(l),abs(r)))
	
print(res)