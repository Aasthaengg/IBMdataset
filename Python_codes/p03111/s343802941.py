n,a,b,c=map(int,input().split())
L=[int(input()) for _ in range(n)]

res2=1000000000

for i in range(2**n-1):
	for j in range(2**n-1):
		x=[]
		y=[]
		z=[]
		for k in range(n):
			
			if i>>k&1:
				if j>>k&1:
					x.append(L[k])
				else:
					y.append(L[k])
			else:
				if j>>k&1:
					z.append(L[k])
		res1=abs(sum(x)-a)+abs(sum(y)-b)+abs(sum(z)-c)
		
		if len(x)==0 or len(y)==0 or len(z)==0:
			continue
	
		if len(x)>1:
			res1+=10*(len(x)-1)
		if len(y)>1:
			res1+=10*(len(y)-1)
		if len(z)>1:
			res1+=10*(len(z)-1)				
		res2=min(res1,res2)

print(res2)