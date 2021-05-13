n, k = map(int, input().split())

def count(a):
  bias = a % k
  if (bias + a) % k:
    return 0
  num = (n - bias) // k 
  if bias > 0:
    num += 1
  return num ** 2

a = 1
res = 0

while(a <= n):
  res += count(a)
  a += 1

print(res)