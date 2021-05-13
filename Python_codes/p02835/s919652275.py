import sys
sys.setrecursionlimit(4100000)
import math
INF = 10**9

def main():
    A = list(map(int, input().split()))

    if sum(A) >= 22:
        print('bust')
    else:
        print('win')


if __name__ == '__main__':
    main()
