import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    X, t = map(int, readline().split())
    print(max(X-t,0))


if __name__ == '__main__':
    main()
