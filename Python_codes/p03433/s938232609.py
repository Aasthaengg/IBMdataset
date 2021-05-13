import sys
sys.setrecursionlimit(4100000)
import math
INF = 10**9

def main():
    n = int(input())
    a = int(input())

    if n%500 <= a:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
