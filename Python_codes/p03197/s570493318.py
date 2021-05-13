import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline

sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N = int(readline())
    A = list(int(readline()) for _ in range(N))
    print('second' if all(A[i] % 2 == 0 for i in range(N)) else 'first')


if __name__ == '__main__':
    main()
