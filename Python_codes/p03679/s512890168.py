import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    X, A, B = map(int, readline().split())

    if B <= A:
        print('delicious')
    elif B <= A + X:
        print('safe')
    else:
        print('dangerous')

    return


if __name__ == '__main__':
    main()
