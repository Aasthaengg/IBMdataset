n,m=map(int,input().split())
l=[]
l=sorted([list(map(int,input().split())) for i in range(m)],key=lambda x:x[1])
ans=1
now=l[0][1]-1

for x,y in l[1:]:
    if x<=now<=y-1:continue
    ans+=1
    now=y-1
print(ans)