a,b,c,k=map(int,input().split())
ans=0

if a>0:
    if (a<k):
        ans+=a
        k-=a
    else:
        ans=k
        print(ans)
        exit()

if b>0:
    if (b<k):
        k-=b
    else:
        print(ans)
        exit()

ans+=(-1)*k
print(ans)