n=int(input())
ti=list(map(int,input().split()))
m=int(input())
p=[]
x=[]
for i in range(m):
  pn,xn=map(int,input().split())
  p.append(pn)
  x.append(xn)
tsum=sum(ti)
for i in range(m):
  sa=ti[p[i]-1]-x[i]
  print(tsum-sa)