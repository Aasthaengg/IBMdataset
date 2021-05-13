import sys
sys.setrecursionlimit(4100000)
import math
INF = 10**9


def main():
    n,m = map(int, input().split())

    print(int(n*(n-1)/2+m*(m-1)/2))


if __name__ == '__main__':
    main()
