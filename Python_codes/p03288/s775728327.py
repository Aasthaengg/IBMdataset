import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    R = int(readline())

    if R < 1200:
        ans = 'ABC'
    elif R < 2800:
        ans = 'ARC'
    else:
        ans = 'AGC'

    print(ans)
    return


if __name__ == '__main__':
    main()
