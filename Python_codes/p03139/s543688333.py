n,a,b=map(int,input().split())

if n < a+b:
	mi=a+b-n
else:
	mi=0

print(min(a,b),mi)