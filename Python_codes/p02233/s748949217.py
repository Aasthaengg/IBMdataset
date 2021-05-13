def fibonacci(n, l):
  if n <= 1:
    l[n] = 1
    return l[n]
  elif l[n] != 0:
    return l[n]
  else:
    l[n] = fibonacci(n-1, l) + fibonacci(n-2, l)
    return l[n]


n = int(input())
l = [0] * (n+1)
print(fibonacci(n, l))
