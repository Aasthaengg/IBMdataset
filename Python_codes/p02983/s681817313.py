L,R=map(int,input().split())
i,j=2020,2020
if R-L+1>=2019:
    print(0)
else:
    ans=float('inf')
    for n in range(L,R+1):
        for m in range(n+1,R+1):
            ans=min(ans,(n*m)%2019)
            
    print(ans)