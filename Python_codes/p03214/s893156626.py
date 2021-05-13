N=int(input())
A=list(map(int,input().split()))
mean=sum(A)/N
d,ans=1000,-1
for i in range(N):
    D=abs(A[i]-mean)
    if D<d:
        d,ans=D,i
print(ans)