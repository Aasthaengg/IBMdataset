import sys
import math


def input():
    return sys.stdin.readline().rstrip()


def main():
    r, D, x = map(int, input().split())
    for i in range(10):
        x = r*x -D
        print(x)



if __name__ == "__main__":
    main()