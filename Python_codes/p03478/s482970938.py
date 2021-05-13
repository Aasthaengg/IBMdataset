n, a, b = map(int, input().split())
count = 0
for i in range(int(n) + 1):
  c = len(str(i))
  d = 0
  for j in range(c):
    d += int(str(i)[j])
  if int(a) <= d and d <= int(b):
    count += i
print(count)