N, A, B = map(int, input().split())
if N < 1 or A > B or (N == 1 and A != B):
  print(0)
else:
  print(B * (N - 1) + A - A * (N - 1) - B + 1)