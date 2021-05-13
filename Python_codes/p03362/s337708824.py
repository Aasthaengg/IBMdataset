def isprime(n):
  for i in range(2, n + 1):
    if n % i == 0:
      return False
    if i * i > n:
      break
  return True
n = int(input())
s = []
for i in range(2, 55556):
  if isprime(i) and i % 5 == 1:
    s.append(i)
    if len(s) == n:
      break
print(*s)
