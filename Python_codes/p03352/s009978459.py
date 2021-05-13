n = int(input())

max_ = 1
for i in range(2, n):
  k = i
  c = 1
  while k <= n:
    k *= i
    c += 1
  if c > 2:
    max_ = max(max_, k//i)
print(max_)