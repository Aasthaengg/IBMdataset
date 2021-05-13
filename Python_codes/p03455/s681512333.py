import sys
sys.setrecursionlimit(4100000)
import math
INF = 10**9

def main():
    a,b = map(int,input().split())

    if a*b%2 == 0:
        print('Even')
    else:
        print('Odd')


if __name__ == '__main__':
    main()
