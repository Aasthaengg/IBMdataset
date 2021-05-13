# -*- coding: utf-8 -*-

def main():
    def _fibonacci(n,cache):
        if n in cache:
            return cache[n]

        elif n == 0 or n == 1:
            ret = 1
            cache[n] = ret
            return ret
        else:
            ret = _fibonacci(n - 1, cache) + _fibonacci(n - 2, cache)
            cache[n] = ret
            return ret

    N = int(raw_input())
    cache = {}
    return _fibonacci(N,cache)

print main()