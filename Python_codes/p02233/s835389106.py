fib = [0 for i in range(45)]
fib[0] = 1
fib[1] = 1
for i in range(2, 45):
  fib[i] = fib[i - 1] + fib[i - 2]
n = int(input())
print(fib[n])
