import sys
from string import ascii_lowercase

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    S = readline().strip()

    s = set(S)
    for c in ascii_lowercase:
        if c not in s:
            print(c)
            return

    print('None')
    return


if __name__ == '__main__':
    main()
