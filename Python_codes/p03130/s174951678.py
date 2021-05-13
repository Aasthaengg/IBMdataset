lista = []
for i in range(3):
  a,b = map(int,input().split())
  lista.append(a)
  lista.append(b)
l1 = 0
l2 = 0
l3 = 0
l4 = 0
for j in lista:
  if j == 1:
    l1 += 1
  if j == 2:
    l2 += 1
  if j == 3:
    l3 += 1
  if j == 4:
    l4 += 1
c = (l1)%2 + (l2)%2 + (l3)%2 + (l4)%2
if c <= 2:
  print('YES')
else:
  print('NO')
  
