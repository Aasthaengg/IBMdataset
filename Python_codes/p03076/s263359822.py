import sys
from math import ceil


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    S = [input() for _ in range(5)]
    mi = 10
    for s in S:
        if not s[-1] == '0':
            mi = min(mi, int(s[-1]))
    S = list(map(lambda x: ceil(int(x) / 10) * 10, S))
    print(sum(S) - (10 - mi))


if __name__ == '__main__':
    main()
