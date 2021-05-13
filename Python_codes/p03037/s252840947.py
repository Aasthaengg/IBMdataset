n,m=map(int,input().split())
a=[]
b=[]
for i in range(m):
  l,r=map(int,input().split())
  a.append(l)
  b.append(r)
ans=min(b)-max(a)+1
print(ans if ans>=0 else 0)