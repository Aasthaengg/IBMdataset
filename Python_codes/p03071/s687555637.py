A, B = map(int, input().split())

if A-B > 0:
  print(2*A-1)
elif B-A > 0:
  print(2*B-1)
elif A-B == 0:
  print(A+B)