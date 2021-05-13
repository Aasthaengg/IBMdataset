import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    S = readline().strip()

    if S[0] != 'A':
        print('WA')
        return

    if S[2 : len(S) - 1].count('C') != 1:
        print('WA')
        return

    if sum(1 for c in S if c.isupper()) != 2:
        print('WA')
        return

    print('AC')
    return


if __name__ == '__main__':
    main()
