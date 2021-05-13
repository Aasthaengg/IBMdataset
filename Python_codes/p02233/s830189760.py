n = int(input())

cache = {0: 1, 1: 1}
def fibonacci(n):
    if cache.get(n, None) is not None:
        return cache[n]
    cache[n] = fibonacci(n-1) + fibonacci(n-2)
    return cache[n]

print(fibonacci(n))