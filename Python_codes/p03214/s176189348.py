n=int(input())
a=list(map(int,input().split()))
p=sum(a)/n
k=[]
for i in range(n):
	k.append(abs(p-a[i]))
for i in range(n):
	if k[i]==min(k):
		print(i)
		break