fib = [1 for i in range(45)]
for i in range(2, 45):
    fib[i] = fib[i - 1] + fib[i - 2]
i = int(input())
print(fib[i])