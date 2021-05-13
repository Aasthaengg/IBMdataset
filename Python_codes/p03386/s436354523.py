a, b, k = map(int, input().split())
for i in range(a, a + k):
  if i <= b:
    print(i)
  else:
    break
for i in range(b - k + 1, b + 1):
  if i >= a + k:
    print(i)
