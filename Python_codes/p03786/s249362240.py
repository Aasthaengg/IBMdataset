N=int(input())
A=list(map(int, input().split()))

A=sorted(A)

ans=1
now=A[0]
sums=A[0]
for i in range(N-1):
    if 2*sums>=A[i+1]:
        ans+=1
        #now+=A[i+1]
    else:
        ans=1
        #now=A[i+1]
    sums+=A[i+1]
print(ans)