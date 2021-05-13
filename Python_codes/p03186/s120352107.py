num = list(map(int, input().split()))
A = num[0]
B = num[1]
C = num[2]

if A + B + 1 >= C:
  print(B + C)
else:
  print(A + 2 * B + 1)