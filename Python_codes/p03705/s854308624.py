N, A, B = list(map(int,input().split()))
if (B * (N-1) + A) - (B + (N-1) * A) < 0:
  print(0)
elif A == B:
  print(1)
else:
  print((B * (N-1) + A) - (B + (N-1) * A) + 1)