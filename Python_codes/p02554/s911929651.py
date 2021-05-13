"""AtCoder Beginner Contest 178.

C
"""

import sys


def input() -> str:  # noqa: A001
    """Input."""
    return sys.stdin.readline()[:-1]


def main():
    """Run."""
    mod = 1000000007
    n = int(input())

    ans = 0

    if n <= 1:
        ans = 0
    elif n == 2:
        ans = 2
    else:
        ans = 10**n
        ans -= 9**n
        ans -= 9**n
        ans += 8**n

    print(ans % mod)


main()
