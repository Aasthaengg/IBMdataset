import sys
import collections

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N, M = [int(x) for x in input().split()]
    AB = [[int(x) for x in input().split()] for _ in range(M)]

    c = collections.Counter()
    for a, b in AB:
        c[a] += 1
        c[b] += 1

    for k in c.keys():
        if c[k] % 2 == 1:
            print("NO")
            return
    else:
        print("YES")


if __name__ == '__main__':
    main()
