n,k=map(int,input().split())
TD=[list(map(int,input().split())) for _ in range(n)]
TD=sorted(TD,key=lambda x:-x[1])
#print(TD)
q=[]
ans=0
v=set()
cnt=0
for t,d in TD[:k]:
    ans+=d
    if t in v:
        q.append(d)
    else:
        v.add(t)

ans+=len(v)**2
cnt=ans
for t,d in TD[k:]:
    if t not in v and len(q)!=0:
        x=q.pop()
        ans+=d+2*len(v)+1-x
        v.add(t)
        cnt=max(ans,cnt)

print(cnt)
