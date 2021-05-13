A, B, C, K = map(int,input().split())
a = [A, B, C]
if K % 2 == 0:
  print(A - B)
else:
  print(B - A)