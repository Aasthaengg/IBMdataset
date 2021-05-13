import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
#sys.setrecursionlimit(10**8)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    s = gete()
    t = gete()

    ans = 0
    for i in range(3):
        if s[i] == t[i]: ans += 1

    print(ans)

if __name__ == "__main__":
    main()