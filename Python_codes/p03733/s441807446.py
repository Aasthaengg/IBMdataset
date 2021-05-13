N,T = map(int,input().split())
A = list(map(int,input().split()))
LST = []

for a in A:
  LST.append((a,1))
  LST.append((a+T,-1))
  
LST.sort()

prev = -1
s = 0
ans = 0
for x,y in LST:
  if y == 1:
    s += 1
    if s == 1:
      prev = x
  elif y == -1:
    s -= 1
    if s == 0:
      ans += (x - prev)
  
print(ans)

