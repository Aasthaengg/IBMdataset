f=lambda:[*map(int,input().split())]
n,m,c=f()
l=f()
a=0
for _ in range(n):
  t=sum(a*b for a,b in zip(f(),l))
  if t+c>0: a+=1
print(a)