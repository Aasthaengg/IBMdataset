from functools import lru_cache
n = int(input())

@lru_cache(maxsize=None)


def fib(n):
    if n==0 or n==1:
        return 1
   
    else:
        return fib(n-1)+fib(n-2)
        
print(fib(n))
