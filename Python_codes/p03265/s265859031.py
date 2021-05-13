MOD = 10 ** 9 + 7
INF = 10 ** 11
import sys
sys.setrecursionlimit(100000000)

def main():
    a,b,c,d = map(int,input().split())
    dx = c - a
    dy = d - b
    print(c - dy,d + dx,a - dy,b + dx)
if __name__ == '__main__':
    main()
