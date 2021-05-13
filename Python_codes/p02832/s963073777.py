n=int(input())

a=[int(x) for x in input().split()]

i=0
ans=0
saigo=0
k=1
kosuu=n

while i<=n-1:
    if a[i]!=k:
        ans+=1
        kosuu-=1
    else:
        saigo=a[i]
        k+=1
    i+=1

if kosuu==0:
    print(-1)
    exit()

if kosuu==saigo:
    print(ans)
else:
    print(-1)