n = int(input())
q = lambda i:input('%d\n'%i)
i, j = 0, n - 1
a, b = q(i), q(j)
while True:
  k = (j - i + 1) // 2 + i
  c = q(k)
  if (k - i)%2 == (a==c):
    j = k
  else:
    a = c
    i = k
