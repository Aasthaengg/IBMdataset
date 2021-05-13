import sys
import collections

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    S = input().strip()

    c = collections.Counter(S)
    c['a'] += 1
    c['a'] -= 1
    c['b'] += 1
    c['b'] -= 1
    c['c'] += 1
    c['c'] -= 1

    if c.most_common()[0][1] - c.most_common()[2][1] >= 2:
        print("NO")
    else:
        print("YES")


if __name__ == '__main__':
    main()

