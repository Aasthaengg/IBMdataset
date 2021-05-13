N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
for i in range(1,N): A[i]+=A[i-1]
for i in range(N-2,-1,-1): B[i]+=B[i+1]
ans=max(A[i]+B[i] for i in range(N))
print(ans)
