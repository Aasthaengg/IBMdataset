maxa=-(10**10)
a,b,n=map(int,input().split())
i=min(n,b-1)
maxa=max(((a*i)//b)-a*(i//b),maxa)
print(maxa)