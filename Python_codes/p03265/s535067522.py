import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    x1, y1, x2, y2 = map(int, readline().split())
    
    dx = x2 - x1
    dy = y2 - y1
    
    x3, y3 = x2 - dy, y2 + dx
    x4, y4 = x1 - dy, y1 + dx
    
    print(x3, y3, x4, y4)
    
    return


if __name__ == '__main__':
    main()
