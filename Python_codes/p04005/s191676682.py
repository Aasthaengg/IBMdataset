A, B, C = map(int, input().split())
if A * B * C % 2 == 0:
  print(0)
else:
  M = max(A, B, C)
  if M == A:
    print(B * C)
  elif M == B:
    print(A * C)
  else:
    print(A * B)