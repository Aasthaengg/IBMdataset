n,k=map(int,input().split())
a=[]
for _ in range(n):a.append(tuple(list(map(int,input().split()))[::-1]))
a.sort(reverse=1)
x,y=[],[]
s=set()
for i in range(k):
  d,t= a[i]
  if t in s:
    x.append(d)
  else:
    y.append(d)
    s.add(t)
xx,yy,v=sum(x),sum(y),len(y)
ans=xx+yy+v**2
for i in range(k,n):
    if len(x)==0:break
    d,t=a[i]
    if t in s:continue
    s.add(t)
    xx-=x.pop()
    yy+=d
    v+=1
    ans=max(ans,xx+yy+v**2)
print(ans)