N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
ans=0
for i in range(N):
    ans+=B[i]
for i in range(N):
    if i==N-1:
        ans+=0
    elif A[i]+1==A[i+1] :
        ans+=C[A[i]-1]
    else :
        ans+=0
print(ans)
