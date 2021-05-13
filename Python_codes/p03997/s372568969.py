import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    a = int(readline())
    b = int(readline())
    h = int(readline())
    print((a+b)*h//2)


if __name__ == '__main__':
    main()
