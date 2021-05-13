n, k, s = map(int, input().split())
for _ in range(k):
  print(s, end=' ')
if s == 10 ** 9:
  for _ in range(n-k):
    print(1, end=' ')
else:
  for _ in range(n-k):
    print(10 ** 9, end=' ')