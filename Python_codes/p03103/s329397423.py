n,m=map(int,input().split())
d={};price=0
for _ in range(n):
  a,b=map(int,input().split())
  if a not in d:
    d[a] = b
  else:
    d[a] += b
d=sorted(d.items(),key=lambda x:x[0])
for i in d:
  for _ in range(i[1]):
    if m == 0:
      print(price)
      exit()
    m-=1
    price+=i[0]
else:
  print(price)