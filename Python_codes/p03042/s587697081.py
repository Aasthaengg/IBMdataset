import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


def main():
    S = readline().strip()
    x = int(S[:2])
    y = int(S[2:])

    if 1 <= x <= 12:
        if 1 <= y <= 12:
            print('AMBIGUOUS')
        else:
            print('MMYY')
    else:
        if 1 <= y <= 12:
            print('YYMM')
        else:
            print('NA')

    return


if __name__ == '__main__':
    main()
