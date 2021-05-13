N=int(input())
a=map(int,input().split())
ans,d=0,{}
for x in a:
    d[x]=d.get(x,0)+1
    ans+=1
    if d[x]==x:
        ans-=x
print(ans)
