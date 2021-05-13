n,p = map(int,input().split())
l = list(map(int,input().split()))
l1 = []
for i in l:
  if i%2==0:
    l1.append(0)
  else:
    l1.append(1)
    


a = l1.count(1)
b = l1.count(0)
if a!=0:
  cou = (2**(b))*(2**(a-1))
  print(cou)
else:
  if p%2==0:
    print(2**b)
  else:
    print(0)