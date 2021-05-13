# 等差等比数列

def input():
    import sys
    return sys.stdin.readline().rstrip()


def main():
    import math
    import collections
    import itertools

    n, m = map(int, input().split())
    print(2 ** m * (18 * m + n) * 100)




if __name__ == '__main__':
    main()