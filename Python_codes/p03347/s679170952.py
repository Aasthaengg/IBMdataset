N=int(input())
A=[int(input()) for i in range(N)]
ans=0

for i in range(N):
    #print(str(i-1)+"  ",end="")
    #print(ans)
    if i==0:
        if A[i]!=0:
            ans=-1
            break
    else:
        if A[i-1]+1 > A[i]:
            ans+=A[i-1]
        elif A[i-1]+1==A[i]:
            continue
        else:#A[i-1]<A[i]:
            ans=-1
            break
else:
    ans+=A[i]
print(ans)
