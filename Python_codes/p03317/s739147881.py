n,k=map(int,input().split())
a=list(map(int,input().split()))
x=a.index(1)
#print(x)

if n==k:
    print(1)
else:
    #if x<=k-1 or x>=n-k:
    if (n-k)%(k-1)==0:
        ans=1+(n-k)//(k-1)
    else:
        ans=1+(n-k)//(k-1)+1


    print(ans)