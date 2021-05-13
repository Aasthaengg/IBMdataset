n=int(input());t,x,y=[],[],[]
for _ in range(n):
  a,b,c=map(int,input().split())
  t.append(a);x.append(b),y.append(c)
for i in range(n):
  m,k=[[t[0],x[0]+y[0]],[t[i]-t[i-1],abs(x[i]-x[i-1])+abs(y[i]-y[i-1])]][i!=0]
  if not (m>=k and m%2==k%2): print('No');break
else:
  print('Yes')