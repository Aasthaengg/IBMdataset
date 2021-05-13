import sys
import math
import itertools

def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    d,m = divmod(N-1,111)

    print((d+1)*111)


if __name__ == "__main__":
    main()
