N=int(input())
*A,=map(int,input().split())

if N<=2:
    ans=1
else:
    ans=1
    count=(A[0]<A[1])-(A[0]>A[1])
    i=2
    while i<N:
        if count*((A[i-1]<A[i])-(A[i-1]>A[i]))<0:
            ans+=1
            count=0
        else:
            if count==0:
                count=(A[i-1]<A[i])-(A[i-1]>A[i])
        i+=1

print(ans)