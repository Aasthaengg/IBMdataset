N, K = map(int, input().split())
L = N//K
if K%2==1:
  print(L**3)
else:
  M = N//(K//2)
  M -= L 
  print(L**3 + M**3)