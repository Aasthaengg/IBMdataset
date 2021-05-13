a,b=input().split()
a=int(a)
b=int(b)
c=list(map(int,input().split()))
d=0
c.sort()
for i in range(b):
  d=d+c[i]
print(d)