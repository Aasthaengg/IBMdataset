def fib(n):
    f0, f1 = 1, 1

    for i in range(n - 1):
        f1, f0 = f1 + f0, f1

    return f1

n = int(input())
ans = fib(n)

print(ans)