import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    S = readline().strip()
    T = readline().strip()

    for i in range(len(S)):
        if S[i:] + S[:i] == T:
            print('Yes')
            return

    print('No')
    return


if __name__ == '__main__':
    main()
