n=int(input())
h=list(map(int,input().split()))
f=True

for i in range(1,n):
	if h[-i]>=h[-i-1]:
		pass
	else:
		h[-i-1]-=1

for i in range(1,n):
	if h[i]>=h[i-1]:
		f=True
	else:
		f=False
		break

if f:
	print('Yes')
else:
	print('No')