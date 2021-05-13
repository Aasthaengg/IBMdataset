A, B = list(map(int,input().split()))
if A >= B + 2:
  print(2 * A - 1)
elif B >= A + 2:
  print(2 * B - 1)
else:
  print(A + B)