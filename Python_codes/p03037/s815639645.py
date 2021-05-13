N, M = map(int, input().split())

for i in range(M):
  L, R = map(int, input().split())
  
  if i == 0:
    top = R
    bottom = L
  
  top = min(top, R)
  bottom = max(bottom, L)

if top >= bottom:
  print(top-bottom+1)
else:
  print(0)