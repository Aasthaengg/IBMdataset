def fib(n, fib_table):
    if n == 0 or n == 1:
        return 1
    if fib_table[n] != None:
        return fib_table[n]
    fib_table[n] = fib(n-1, fib_table) + fib(n-2, fib_table)
    return fib_table[n]

n = int(input())
fib_table = [None]*(n+1)
fib_table[0] = 1
fib_table[1] = 1

print(fib(n, fib_table))