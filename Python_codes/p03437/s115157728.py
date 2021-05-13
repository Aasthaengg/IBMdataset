import collections
import math


def main():
    x, y = map(int, input().split())

    if x % y == 0:
        print(-1)
        return
    print(x)


if __name__ == '__main__':
    main()
