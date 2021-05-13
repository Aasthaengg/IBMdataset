a,b,k=map(int,input().split())
al=a+k
bs=b-k
if k>(b-a)/2:
	for i in range(a,b+1):
		print(i)
else:
	for i in range(a,al):
		print(i)
	for j in range(bs+1,b+1):
		print(j)