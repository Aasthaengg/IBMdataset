import sys
from collections import Counter
from functools import lru_cache

c = None

@lru_cache(maxsize=200000)
def _num_of_ways_to_choose(x):
    v = c[x]
    return (v * (v - 1)) // 2


def resolve(in_, out):
    n = int(in_.readline())
    a = tuple(map(int, in_.readline().split()))
    global c
    c = dict(Counter(a))

    _num_of_ways_to_choose.cache_clear()
    total = sum(map(_num_of_ways_to_choose, c.keys()))

    for ai in a:
        ans = total - _num_of_ways_to_choose(ai) + ((c[ai] - 1) * (c[ai] - 2)) // 2
        print(ans, file=out)


def main():
    resolve(sys.stdin.buffer, sys.stdout)


if __name__ == '__main__':
    main()
