import sys
import numpy as np


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(10 ** 9)


def main():
    x, y = map(int, input().split())
    if x > 0:
        if y > 0:
            if x > y:
                answer = x - y + 2
            else:
                answer = y - x
        elif y == 0:
            answer = x + 1
        else:
            if -x <= y:
                answer = y + x + 1
            else:
                answer = abs(y) - x + 1
    elif x == 0:
        if y > 0:
            answer = y
        else:
            answer = -y + 1
    else:
        if y > 0:
            if abs(x) >= y:
                answer = abs(x) - y + 1
            else:
                answer = y - abs(x) + 1
        elif y == 0:
            answer = abs(x)
        else:
            if abs(x) > abs(y):
                answer = abs(x) - abs(y)
            else:
                answer = abs(y) - abs(x) + 2
    print(answer)


if __name__ == "__main__":
    main()
