N, A, B = map(int, input().split())
if A > B:
  print(0)
  exit()
if N == 1 and A != B:
  print(0)
  exit()
s1 = A * (N - 1) + B
s2 = B * (N - 1) + A
print(s2 - s1 + 1)