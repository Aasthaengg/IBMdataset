import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    A, B = map(int, read().split())

    if A % 3 == 0 or B % 3 == 0 or (A + B) % 3 == 0:
        print('Possible')
    else:
        print('Impossible')

    return


if __name__ == '__main__':
    main()
