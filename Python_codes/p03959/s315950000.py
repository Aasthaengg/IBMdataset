def ex():
    print(0)
    exit()

MOD=10**9+7
N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
if N==1:
    print(1 if A[0]==B[0] else 0)
    exit()

ans=1
tmp=[-1]*N
for i in range(N):
    if i==0 or (i>0 and A[i-1]<A[i]):
        if B[i]<A[i]:
            ex()
        tmp[i]=A[i]
for i in reversed(range(N)):
    if i==N-1 or (i<N-1 and B[i]>B[i+1]):
        if tmp[i]!=-1 and tmp[i]!=B[i]:
            ex()
        if A[i]<B[i]:
            ex()
        tmp[i]=B[i]
for i in range(N):
    if tmp[i]==-1:
        ans=ans*min(A[i],B[i])%MOD
print(ans)
