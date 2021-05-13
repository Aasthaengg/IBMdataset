import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
geta = lambda fn: map(fn, readline().split())
gete = lambda fn: fn(input())

# sys.setrecursionlimit(10**5)


def main():
    S = gete(str)[::-1]
    m, mod = 13, 10**9 + 7
    prev, curr = [0] * m, [0] * m
    base = []

    s0, b = 0, 1
    for i, c in enumerate(S):
        if c == "?":
            base.append(b)
        else:
            s0 = (s0 + b * int(c)) % m
        b = (b * 10) % m
    curr[s0] = 1

    for b in base:
        prev, curr = curr, [0] * m

        for d in range(10):
            ad = d * b
            for r, p in enumerate(prev):
                curr[(r + ad) % m] += p

            for r, c in enumerate(curr):
                curr[r] = c % mod

    print(curr[5])


if __name__ == "__main__":
    main()
