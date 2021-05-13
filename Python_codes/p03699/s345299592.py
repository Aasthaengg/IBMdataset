n=int(input())
a=[]
b=[]
d=0
for i in range(n):
  c=int(input())
  d+=c
  if c%10==0:
    a.append(c)
  else:
    b.append(c)
b.sort()
if d%10==0 and b:
  print(d-b[0])
elif d%10==0:
  print(0)
else:
  print(d)