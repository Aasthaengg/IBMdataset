L,R=map(int,input().split())
n=2019
if R-L>=2019:
    print(0)
else:
    L%=n
    R%=n
    if L>=R:
        print(0)
    else:
        ans=(L*R)%n
        for i in range(L,R+1):
            for j in range(i+1,R+1):
                ans=min(ans,i*j%n)
        print(ans)