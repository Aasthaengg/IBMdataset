a, b = map(int, input().split())
A = a+b
if A > 24:
  print(A-24)
elif A < 24:
  print(A)
elif A == 24:
  print("0")