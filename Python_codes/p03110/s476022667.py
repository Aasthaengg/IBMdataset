n=int(input())

b=380000
res=0

for _ in range(n):
	x,u=input().split()
	x=float(x)
	if u=="BTC":
		x*=b
	res+=x
	
print(res)