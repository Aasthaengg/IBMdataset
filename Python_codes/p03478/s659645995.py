def sumofdigits(n):
  s = 0
  while n > 0:
    s += n % 10
    n = n // 10
  return s

n, a, b = map(int, input().split())

f = 0
for i in range(1, n+1):
  s = sumofdigits(i)
  if s >= a and s <= b:
    f += i
print(f)