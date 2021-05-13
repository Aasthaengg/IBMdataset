import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    A, B, C = map(int, readline().split())
    K = int(readline())
    print(max(A, B, C) * 2**K + A+B+C-max(A,B,C))


if __name__ == '__main__':
    main()
