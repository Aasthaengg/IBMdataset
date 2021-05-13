L,R=map(int,input().split())
l=L%2019
r=R%2019
#print(l,r)
if l<r and L//2019 == R//2019:
    ans=10**18
    for i in range(l,r):
        for j in range(l+1,r+1):
            if ans>(i*j)%2019:
                ans=(i*j)%2019
    print(ans)
elif L//2019<R//2019:
    print(0)
