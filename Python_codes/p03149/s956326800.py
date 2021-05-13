A = list(map(int, input().split()))
A1 = A.count(1)
A9 = A.count(9)
A7 = A.count(7)
A4 = A.count(4)
if A1 == A9 == A7 == A4 == 1:
  print("YES")
else:
  print("NO")