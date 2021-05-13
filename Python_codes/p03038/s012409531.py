n,m=map(int,input().split())
a=list(map(int,input().split()))
d={}
for i in a:
  d[i]=d.get(i,0)+1

for _ in range(m):
    b,c=map(int,input().split())
    d[c]=d.get(c,0)+b
e=list(d.keys())
e.sort()
ans=f=0
for i in e[::-1]:
    if f+d[i]>=n:
        ans+=i*(n-f)
        break
    ans+=i*d[i]
    f+=d[i]
print(ans)