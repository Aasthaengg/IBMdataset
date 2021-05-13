N, A, B = map(int, input().split())
S = N*A
if B < S or B == S:
  print(B)
else:
  print(S)