A, B, C = map(int, input().split())
if A == B == C:
  print("No")
elif A == B or B == C or C == A:
  print("Yes")
else:
  print("No")
