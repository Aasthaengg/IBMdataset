N, K = map(int, input().split())
 
if K % 2 == 1:
  a = N // K
  print(a**3)
else:
  a = N // K
  if K*a + K//2 <= N:
    b = a + 1
  else:
    b = a
  print(a**3 + b**3)