N,K=map(int,input().split())
P=list(map(int,input().split()))
A=[]
for num in P:
    num=(num+1)*0.5
    A.append(num)

T=sum(A[:K])
ans=sum(A[:K])
for i in range(N-K):
    a=T-A[i]+A[i+K]
    ans=max(ans,a)
    T=a
print(ans)