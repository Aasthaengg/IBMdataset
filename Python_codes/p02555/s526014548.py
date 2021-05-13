"""AtCoder Beginner Contest 178.

D
"""

import sys


def input() -> str:  # noqa: A001
    """Input."""
    return sys.stdin.readline()[:-1]


def main():
    """Run."""
    mod = 1000000007
    s = int(input())

    a = [0] * (s + 1)
    a[0] = 1

    for i in range(3, s + 1):
        a[i] = a[i - 3] + a[i - 1]

    print(a[s] % mod)


main()
