N, A, B = map(int, input().split())

if B < A:
  print(0)
elif N == 1 and A!= B:
  print(0)
elif N == 1 and A == B:
  print(1)
else:
  print(1 + ( N - 2) * (B - A))
