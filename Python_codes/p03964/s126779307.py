N=int(input())
T=[]

A=[1,1]

for i in range(N):
	t=list(map(int,input().split()))
	
	n0 = (A[0]-1)//t[0] + 1
	n1 = (A[1]-1)//t[1] + 1
	n = max(n0,n1)

	A[0]=t[0]*n
	A[1]=t[1]*n


print(sum(A))