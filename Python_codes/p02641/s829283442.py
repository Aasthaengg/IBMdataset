x, n = map(int, input().split( ))
if n == 0:
  print(x)
  exit()
P = list(map(int, input().split( )))

if x not in P:
  print(x)
  exit()
i,c = 1, 0
while i <= n:
  m = x - i
  l = x + i
  if m not in P:
    print(m)
    break
  elif l not in P:
    print(l)
    break
  i += 1
