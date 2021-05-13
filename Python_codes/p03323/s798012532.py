a,b = map(int,input().split())
A = max(a,b)
B = min(a,b)
res = 16
while True:
  A -= 1
  res -= 1
  B -= 1
  res -= 1
  if B == 0: break
    
if A <= res//2:
  print("Yay!")
else:
  print(":(")