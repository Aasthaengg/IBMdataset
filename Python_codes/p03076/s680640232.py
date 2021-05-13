x = [int(input()) for i in range(5)]
y=0
for i in x:
  if i%10==0:
    y+=i
  else:
    y+=(i+(10-(i%10)))
a=[]
for i in x:
  a.append(i%10)
if a.count(0)!=5:
  while 0 in a:
    a.remove(0)
  b=sorted(a)
  print(y-(10-b[0]))
else:
  print(y)
