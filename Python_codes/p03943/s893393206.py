a, b, c = map(int, input().split())

S = a + b + c
M = max([a, b, c])
if S - M == M:
  print("Yes")
else:
  print("No")
  
  
  

