n,k=map(int,input().split())
c=int(n/k)
if(k%2==1):
    print(c*c*c)
else:
    ans=c*c*c
    c=int((n+k/2)/int(k))
    print(c*c*c+ans)
