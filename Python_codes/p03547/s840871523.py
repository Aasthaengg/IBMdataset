import sys
sys.setrecursionlimit(4100000)
import math
INF = 10**9

def main():
    x,y = input().split()

    if x == y:
        print('=')
    elif x < y:
        print('<')
    else:
        print('>')


if __name__ == '__main__':
    main()
