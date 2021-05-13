import sys
from collections import defaultdict


g = None
memo = None


def f(x):
    if memo[x] == -1:
        ret = 0
        for y in g[x]:
            ret = max(ret, f(y) + 1)
        memo[x] = ret
    return memo[x]


def resolve(in_):
    global g, memo
    n, m = map(int, next(in_).split())
    _g = defaultdict(list)
    for line in in_:
        x, y = map(int, line.split())
        _g[x - 1].append(y - 1)
    g = _g
    memo = [-1] * 100000
    return max(f(i) for i in range(n))


def main():
    sys.setrecursionlimit(1000000)
    ans = resolve(sys.stdin.buffer)
    print(ans)


if __name__ == '__main__':
    main()
