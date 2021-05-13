N, M = map(int, input().split())
left = []
right = []
for i in range(M):
  a, b = map(int, input().split())
  if a == 1:
    left.append(b)
  elif b == N:
    right.append(a)
    
flag = False
left = set(left)
for r in right:
  if r in left:
    flag = True
    break
    
if flag:
  print('POSSIBLE')
else:
  print('IMPOSSIBLE')
