import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


def main():
    s = int(input())

    def f(y):
        if y % 2 == 0:
            a = y // 2
        else:
            a = 3 * y + 1
        return a

    ss = set()
    ss.add(s)

    for i in range(10 ** 8):
        s = f(s)
        if s in ss:
            print(i+2)
            exit()
        ss.add(s)



if __name__ == "__main__":
    main()
