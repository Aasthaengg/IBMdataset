import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N = int(readline())
    contest = N // 1000
    if contest >= 1:
        print('ABD')
    else:
        print('ABC')


if __name__ == '__main__':
    main()
