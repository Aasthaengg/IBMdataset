import sys
sys.setrecursionlimit(4100000)
import math
INF = 10**9

def main():
    a,b,k = map(int,input().split())

    num = min(a,k)
    a -= num
    k -= num
    b -= min(b,k)
    print(a,b)


if __name__ == '__main__':
    main()
