import math
import sys
readline = sys.stdin.readline


def main():
    x = int(readline().rstrip())
    a, b, c = 0, 0, 1

    while a < 1000:
        k = a ** 5 - x
        c = 1 if k >= 0 else - 1
        b = abs(k) ** 0.2
        if int(b) ** 5 == abs(k):
            print(a, c * abs(int(b)))
            return
        a += 1


if __name__ == '__main__':
    main()
