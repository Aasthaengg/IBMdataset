_fib = [None] * 45
_fib[0] = 1
_fib[1] = 1

def fib(n):
    if _fib[n] is None:
        _fib[n] = fib(n-1) + fib(n-2)
    return _fib[n]

_n = int(raw_input())
print(fib(_n))