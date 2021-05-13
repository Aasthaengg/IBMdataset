n,h,w=map(int,input().split())

cnt=0
a=[]
b=[]

for i in range(n):
  c,d=map(int,input().split())
  a.append(c)
  b.append(d)

for i in range(n):
  e=int(a[i]/h)
  f=int(b[i]/w)
  cnt=cnt+min(e,f)
print(cnt)