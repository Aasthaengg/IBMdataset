def fib(n):
  if F[n] != 0:
    return F[n]
  elif n==0 or n==1:
    F[n] = 1
  else:
    F[n] = fib(n-1) + fib(n-2)

  return F[n]



n = input()
F = [0 for row in range(n+1)]
print fib(n)