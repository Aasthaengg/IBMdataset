def gcd(_a, _b):
	if _a%_b==0:return _b
	else:return gcd(_b, _a%_b)

n=int(input())
a=sorted(map(int,input().split()))
INF=2*10**9
ans=INF
for i in range(len(a)-1):
	tmp=gcd(a[i],a[i+1])
	if tmp!=0 and tmp<ans:
		ans=tmp
print(ans)