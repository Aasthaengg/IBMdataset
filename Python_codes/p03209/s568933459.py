n, x = map(int, input().split())
a, p = [1], [1]
for i in range(n):
 a += [a[i] * 2 + 3]
 p += [p[i] * 2 + 1]

def f(n, x):
 if n == 0:
  return 1 - (x <= 0)
 elif x <= 1 + a[n-1]:
  return f(n-1, x-1)
 else:
  return p[n-1] + 1 + f(n-1, x-2-a[n-1])

print(f(n, x))