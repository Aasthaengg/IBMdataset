n,m=map(int,input().split())
s,t=0,100001
for i in range(m):
    l,m=map(int,input().split())
    if l>s:
        s=l
    if m<t:
        t=m

ans=t-s+1
if ans<0:
    ans=0
print(ans)