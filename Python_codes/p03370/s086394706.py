n,x = map(int,input().split())
m = [0]*n

for i in range(n):
  m[i] = int(input())
c = 0
if sum(m) >= x:
  for i in range(n):
    if x >= 0:
      x = x - m[i]
      c += 1
    else:
      break
  print(c)
else:
  x = x - sum(m)
  c = len(m)
  c += int(x/min(m))
  print(c)