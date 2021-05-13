import sys
from functools import lru_cache
from collections import defaultdict


g = None


@lru_cache(100000)
def f(x):
    ret = 0
    for y in g[x]:
        ret = max(ret, f(y) + 1)
    return ret


def resolve(in_):
    global g
    n, m = map(int, next(in_).split())
    _g = defaultdict(list)
    for line in in_:
        x, y = map(int, line.split())
        _g[x - 1].append(y - 1)
    g = _g
    f.cache_clear()
    return max(f(i) for i in range(n))


def main():
    sys.setrecursionlimit(1000000)
    ans = resolve(sys.stdin.buffer)
    print(ans)


if __name__ == '__main__':
    main()
