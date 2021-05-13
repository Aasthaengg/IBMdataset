N,A,B=open(0).read().rstrip().split('\n')
N=int(N)
A=list(map(int,A.split()))
B=list(map(int,B.split()))
hunt=0
for i in range(N):
    if A[i]>=B[i]:
        hunt+=B[i]
    elif A[i]+A[i+1]>=B[i]:
        hunt+=B[i]
        suplus=B[i]-A[i]
        A[i+1]=A[i+1]-suplus
    else:
        hunt+=A[i]+A[i+1]
        A[i+1]=0
print(hunt)