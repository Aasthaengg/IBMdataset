S, T = map(str, input().split())
A, B = map(int, input().split())
U = str(input())
if S == U:
  A = A - 1
  print(A, B)
elif T == U:
  B = B - 1
  print(A, B)
else:
  pass