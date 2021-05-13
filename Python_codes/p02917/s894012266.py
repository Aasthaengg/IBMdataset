N=int(input())
B=list(map(int, input().split()))
INF=float('inf')
A=[(-1)*INF]*N
A[0]=A[1]=B[0]
for i in range(1,N-1):
    A[i+1]=B[i]
    A[i]=min(A[i],A[i+1])
print(sum(A))