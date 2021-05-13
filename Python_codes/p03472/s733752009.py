n,h = map(int,input().split())
l = sorted([list(map(int,input().split())) for _ in range(n)])[::-1]
a,b = l[0]
cou = 0
if b>=h:
  print(1)
  exit()
l1 = sorted([i for j,i in l[1:]])[::-1]
for k in l1:
  if a<k:
    cou += 1
    h -= k
    if h<=0:
      print(cou)
      exit()
    elif h-b<=0:
      print(cou+1)
      exit()
h -= b
cou += 1
if h<=0:
  print(cou)
else:
  t = -(-h//a)
  print(cou+t)