N,Q=map(int,input().split())
S=input()
A=[0]*N
for i in range(1,N+1):
	if S[i-1:i+1]=="AC":
		A[i]+=1
for i in range(1,N):
	A[i]=A[i]+A[i-1]
for i in range(Q):
	l,r=map(int,input().split())
	print(A[r-1]-A[l-1])