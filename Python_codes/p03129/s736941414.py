import sys
import math

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N, K = map(int, readline().split())
    if math.ceil(N/2)>=K:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
