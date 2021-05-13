import sys
sys.setrecursionlimit(4100000)
import math
INF = 10**9

def main():
    x = int(input())
    a = int(input())
    b = int(input())

    print((x-a)%b)


if __name__ == '__main__':
    main()
