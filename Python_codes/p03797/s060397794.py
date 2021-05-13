n,m=map(int,input().split())
if n>m//2:
    print(m//2)
else:
    ans=n
    tmp=m-(n*2)
    ans+=tmp//4
    print(ans)