import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    a, b = map(int, readline().split())
    if a>b:
        print(a-1)
    else:
        print(a)


if __name__ == '__main__':
    main()
