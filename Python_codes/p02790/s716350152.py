a, b = map(str, input().split())

A = int(a*(int(b)))
B = int(b*(int(a)))

if A <= B:
  print(B)
else:
  print(A)