import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
# sys.setrecursionlimit(10**5)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    s = gete()

    ans = 0
    for i in range(len(s) // 2):
        if s[i] != s[-1 - i]:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()