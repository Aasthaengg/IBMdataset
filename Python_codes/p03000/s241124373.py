N,X=map(int,input().split())
L=list(map(int,input().split()))
d=0
i=0
ans=0


while d<=X:
    ans+=1
    d+=L[i]
    i+=1
    if i==N:
        if d<=X:
            ans+=1
        break


print(ans)
