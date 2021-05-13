n=int (input())
A=list(map(int,input().split()))
q=int (input())
m=list(map(int,input().split()))

box=[]
for i in range(2**n):
	b = '{0:0{1}b}'.format(i,n)
	tmp=[]
	for j in range(n):
		if b[j]=='1':
			if b[j]=='1':
				tmp.append(A[j])
	box.append(sum(tmp))
	
for k in m:
	if k in box:
		print("yes")
	else:
		print("no")
