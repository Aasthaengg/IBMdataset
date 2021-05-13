n,m=map(int,input().split())
x=[0]*n
y=[0]*n
z=[0]*n
for i in range(n):
  x[i],y[i],z[i]=map(int,input().split())
ans=0
d=[(1,1,1),(-1,1,1),(1,-1,1),(1,1,-1),(-1,-1,1),(1,-1,-1),(-1,1,-1),(-1,-1,-1)]
for p,q,r in d:
  ans=max(ans,sum(sorted([p*x[i]+q*y[i]+r*z[i] for i in range(n)])[::-1][:m]))
print(ans)