def fib_iter(n):
  fib_n  = 1
  fib_n2 = 1
  fib_n1 = 1
  for i in range(n - 1):
    fib_n  = fib_n1 + fib_n2
    fib_n2 = fib_n1
    fib_n1 = fib_n
  return fib_n

x = int(raw_input())

print fib_iter(x)