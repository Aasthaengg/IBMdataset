from operator import itemgetter
n,m=map(int,input().split())
li=[list(map(int, input().split())) for i in range(n)]
li.sort(key=itemgetter(0))
ans=0
i=0
for i in li:
    a,b=i[0],i[1]
    if m>=b:
        ans+=a*b
        m-=b
    else:
        ans+=a*m
        break
print(ans)

