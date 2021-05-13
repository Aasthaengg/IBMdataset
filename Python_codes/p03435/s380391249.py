c = list(map(int, input().split()))
x, y, z = c[0]-c[1], c[1]-c[2], c[2]-c[0]
flag = True
for i in range(2):
  c = list(map(int, input().split()))
  s, t, u = c[0]-c[1], c[1]-c[2], c[2]-c[0]
  if (x!=s) or (y!=t) or (z!=u):
    flag = False
    break
    
if flag:
  print('Yes')
else:
  print('No')