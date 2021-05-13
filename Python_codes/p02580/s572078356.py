h,w,m=map(int,input().split())
a=[0]*h;b=[0]*w
s=set()
for _ in range(m):
  x,y=map(lambda x:int(x)-1,input().split())
  a[x]+=1;b[y]+=1
  s.add(x*10**6+y)
ma=max(a);mb=max(b)
c=[i for i,v in enumerate(a) if v==ma]
d=[i for i,v in enumerate(b) if v==mb]
for x in c:
  for y in d:
    if not(x*10**6+y in s):
      print(ma+mb)
      exit()
print(ma+mb-1)