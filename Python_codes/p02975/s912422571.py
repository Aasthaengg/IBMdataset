x=int(input())
t=0
a=list(map(int, input().split()))
for i in range(x):
	t=t^a[i]
if t==0:
	print('Yes')
else:
	print('No')