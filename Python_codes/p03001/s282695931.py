import sys
import math


def input():
    return sys.stdin.readline().rstrip()


def main():
    W, H, x, y = map(int, input().split())

    t = H*W
    if W/2 ==x and H/2 ==y:
        print(t/2,1)
    else:
        print(t/2,0)


if __name__ == "__main__":
    main()
