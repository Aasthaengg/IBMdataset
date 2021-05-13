n,m=map(int,input().split())
a=[]
for i in range(n):
  b=[int(x) for x in input().split()]
  a+=b[1:]
c=0
for j in range(m):
  if a.count(j+1)==n:
    c+=1
print(c)    