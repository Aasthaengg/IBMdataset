n,m=map(int,input().split())
l=[]
r=[]
for j in range(m):
    templ,tempr=map(int,input().split())
    l.append(templ)
    r.append(tempr)
ans=min(r)-max(l)+1
if ans<0:
    ans=0
print(ans)