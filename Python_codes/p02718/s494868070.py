n,m = map(int,input().split())
a = sorted(list(map(int,input().split())),reverse=True)
b = sum(a)/(4*m)
c=[]
for i in a[:m]:
  if i >= b:
    c.append(i)

if len(c) == m:
  print('Yes')
else:
  print('No')
