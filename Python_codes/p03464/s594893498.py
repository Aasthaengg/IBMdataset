n=int(input())
a=list(reversed(list(map(int,input().split()))))
p,q=2,2
for i in range(n):
	q2=((q-1)//a[i]+1)*a[i]
	p2=(p//a[i]+1)*a[i]-1
	p=p2
	q=q2
	if p<q:
		print(-1)
		break
else:
	print(q,p)