import sys
from string import ascii_uppercase

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())
    S = readline().strip()

    ans = [0] * len(S)
    for i, c in enumerate(S):
        ans[i] = ascii_uppercase[(ascii_uppercase.index(c) + N) % 26]

    print(''.join(ans))
    return


if __name__ == '__main__':
    main()
