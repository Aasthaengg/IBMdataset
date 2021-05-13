N,x = map(int,input().split())
A = list(map(int,input().split()))
A_org = sum(A)
if A[0]>x:
	A[0]=x
for i in range(N-1):
	if A[i]+A[i+1]>x:
		A[i+1] = x-A[i]

print(A_org-sum(A))
