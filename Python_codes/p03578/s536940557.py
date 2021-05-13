N = int(input())
D = list(map(int,input().split()))
M = int(input())
T = list(map(int,input().split()))

D.sort()
T.sort()

ok = True
idx = 0
for t in T:
  hasSame = False
  while idx <= N-1 and D[idx] <= t:
    d = D[idx]
    idx += 1
    if d == t:
      hasSame = True
      break

  if not hasSame:
    ok = False
    break
      
if ok:
  print('YES')
else:
  print('NO')