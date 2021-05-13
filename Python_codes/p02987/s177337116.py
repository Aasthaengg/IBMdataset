import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    S = readline().strip()

    if (
        S[0] == S[1]
        and S[2] == S[3]
        and S[1] != S[2]
        or S[0] == S[2]
        and S[1] == S[3]
        and S[0] != S[1]
        or S[0] == S[3]
        and S[1] == S[2]
        and S[0] != S[1]
    ):
        print('Yes')
    else:
        print('No')

    return


if __name__ == '__main__':
    main()
