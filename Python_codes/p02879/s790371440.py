A, B = map(int, input().split())
if A > 9 or B > 9:
  print(-1)
  exit()
else:
  print(A*B)