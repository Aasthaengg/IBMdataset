n=int(input())
L=list(map(int, input().split()))
a=max(L)
b=a
c=0
for i in range(n):
	if b>=abs(L[i]-a/2) and L[i]!=a:
		b=abs(L[i]-a/2)
		c=L[i]


print(a,c)
