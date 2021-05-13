MM = input()
LL = input()
M = list(MM)
L = list(LL)
kara =[]
a = len(M)
b = len(L)
x = a + b
for i in range(x):
  if i%2==0:
    aa = M.pop(0)
    kara.append(aa)
  else:
    bb = L.pop(0)
    kara.append(bb)
for i in kara:
  print(i,end='')