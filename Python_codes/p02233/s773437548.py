# -*- coding:utf-8 -*-


def memoize(proc):
    cache = {}

    def helper(*args, **kargs):
        if args not in cache:
            cache[args] = proc(*args, **kargs)
        return cache[args]

    return helper


@memoize
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    print(fib(int(input())))