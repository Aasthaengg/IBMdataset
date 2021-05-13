A, B, C= map(int, input().split())
if A*C <= B:
  print(C)
elif A <= B:
  print(B//A)
else:
  print(0)