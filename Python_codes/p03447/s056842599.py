import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    X = int(readline())
    A = int(readline())
    B = int(readline())
    print((X-A)%B)


if __name__ == '__main__':
    main()
