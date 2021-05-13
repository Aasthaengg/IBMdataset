A, B, C, K = map(int, input().split())
X0 = A + B + C
if abs(A - B) > 10 ** 18:
  print('Unfair')
else:
  print((A - B) * ((-1) ** K))