import math
import sys
readline = sys.stdin.readline


def main():
    x = int(readline().rstrip())
    ans = x // 100
    if ans == 0:
        print(0)
        return

    sur = x - ans * 100
    print(1 if sur / ans <= 5 else 0)


if __name__ == '__main__':
    main()
