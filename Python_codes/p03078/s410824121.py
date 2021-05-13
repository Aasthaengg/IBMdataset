from heapq import nlargest
x,y,z,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
ab=nlargest(k,(x+y for x in a for y in b))
abc=nlargest(k,(x+y for x in ab for y in c))
for i in abc:
  print(i)