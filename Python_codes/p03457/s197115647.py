n=int(input());t,x,y=[],[],[]
for _ in range(n):
  a,b,c=map(int,input().split())
  t.append(a);x.append(b),y.append(c)
for i in range(n):
  if i==0:
    r1,r2=t[i],x[i]+y[i]
  else:
    r1,r2=t[i]-t[i-1],abs(x[i]-x[i-1])+abs(y[i]-y[i-1])
  if not (r1>=r2 and r1%2==r2%2):
    print('No');break
else:
  print('Yes')