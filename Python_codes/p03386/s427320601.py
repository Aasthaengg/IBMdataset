a,b,k=map(int,input().split())
d=set()
f=min(b-a+1,k)
for i in range(f):
  d.add(a+i)
for i in range(f):
  d.add(b-i)
d=sorted(list(d))
for i in d:
  print(i)
