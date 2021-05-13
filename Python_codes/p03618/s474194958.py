import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a = input()
    n = len(a)
    total = (n - 1) * n // 2 + 1

    D = Counter(a)
    for v in D.values():
        total -= (v - 1) * v // 2
    print(total)


if __name__ == '__main__':
    resolve()
