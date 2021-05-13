from string import ascii_lowercase
from itertools import accumulate


def solve(string):
    n = int(string)
    t = [0] + [len(ascii_lowercase)**i for i in range(1, 12)]
    *t, = accumulate(t)
    l = 0
    ans = ""
    while t[l] < n:
        l += 1
    n -= t[l - 1] + 1
    for i in range(l - 1):
        j, n = divmod(n, len(ascii_lowercase)**(l - i - 1))
        ans += ascii_lowercase[j]
    ans += ascii_lowercase[n]
    return ans


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
