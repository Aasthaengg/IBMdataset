import sys
sys.setrecursionlimit(4100000)
import math
INF = 10**9

def main():
    n = int(input())
    k = int(input())

    num = 1
    for i in range(n):
        if num < k:
            num *= 2
        else:
            num += k
    print(num)


if __name__ == '__main__':
    main()
