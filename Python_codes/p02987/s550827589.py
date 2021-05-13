A = list(input())
B = set(A)
if len(B) == 2 and A.count(A[0]) == 2:
  print("Yes")
else:
  print("No")
