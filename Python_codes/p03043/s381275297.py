import sys
import math
import itertools


def input():
    return sys.stdin.readline().rstrip()


def main():
    N, K = map(int, input().split())

    ans =0
    for i in range(1,N+1):
        if i>K:
            s =0
        else:
            s =math.ceil(math.log2(K/i))
        ans +=(0.5 **s ) /N

    print(ans)


if __name__ == "__main__":
    main()
