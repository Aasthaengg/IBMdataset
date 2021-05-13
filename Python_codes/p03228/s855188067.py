a, b, k = map(int, input().split())

def exchange(n, m):
  if n % 2:
    n = (n-1) // 2
  else:
    n = n // 2
  m += n
  return n, m


for i in range(k):
  if i % 2:
    b, a = exchange(b, a)
  else:
    a, b = exchange(a, b)

print('{0} {1}'.format(a, b))
