[n,a,b]=list(map(int,input().split()))
xlist=list(map(int,input().split()))
ans=0
for i in range(1,n):
    walk=(xlist[i]-xlist[i-1])*a
    if (walk<b): #歩いたほうが楽
        ans+=walk
    else:
        ans+=b
ans=int(ans)
print(ans)