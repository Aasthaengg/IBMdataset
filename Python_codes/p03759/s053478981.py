a,b,c = map(int, input().split())

A = [a,b,c]
A.sort()
if A[2] - A[1] == A[1] - A[0]:
  print("YES")
else:
  print("NO")
