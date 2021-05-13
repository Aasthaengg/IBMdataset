A, B, C = map(int, input().split())
mx = max(A, B, C)
if mx == A:
  print(10*A + B + C)
elif mx == B:
  print(10*B + C + A)
else:
  print(10*C + A + B)