A, B, C = [int(i) for i in input().split()]

if A + B >= C - 1:
  print(B + C)
else:
  print(A + 2 * B + 1)