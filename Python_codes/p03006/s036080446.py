import sys
from collections import defaultdict

read = sys.stdin.read
readline = sys.stdin.buffer.readline

sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N = int(readline())
    if N==1:
        print(1)
        sys.exit()
    XY = list(list(map(int, readline().split())) for _ in range(N))
    d = defaultdict(int)
    for i in range(N-1):
        x1, y1 = XY[i]
        for j in range(i+1,N):
            x2, y2 = XY[j]
            x = x2-x1
            y = y2-y1
            d[x,y] += 1
            d[-x,-y] += 1
    print(N-max(d.values()))



if __name__ == '__main__':
    main()
