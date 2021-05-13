n,m=map(int,input().split())
if 2*n>=m:
    print(m//2)
else:
    x=(m-2*n)//4
    ans=min(n+x,(m-2*x)//2)
    x+=1
    anser=min(n+x,(m-2*x)//2)
    print(max(ans,anser))

