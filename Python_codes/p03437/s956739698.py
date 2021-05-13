import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    X, Y = map(int, readline().split())
    if X % Y == 0:
        print('-1')
    else:
        print(X)


if __name__ == '__main__':
    main()
