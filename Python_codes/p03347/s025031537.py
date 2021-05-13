N=int(input())
A=[int(input()) for i in range(N)]
r=0
for i in range(N-1,0,-1):
    if A[i-1]<A[i]-1:
        r=-1
        break
    elif A[i-1]==A[i]-1:
        r+=1
    else:
        r+=A[i]
print(-1 if A[0]!=0 else r)