L = []
for _ in range(3):
  A,B = map(int,input().split()) 
  L.append(A)
  L.append(B)
L.sort()
M = []
a = L.count(1)
b = L.count(2)
c = L.count(3)
d = L.count(4)
M.append(a)
M.append(b)
M.append(c)
M.append(d)
M.sort()
if M == [1,1,2,2]:
  print('YES')
else:
  print('NO')
