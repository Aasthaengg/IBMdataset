import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())
    S = readline().strip()

    ans = 0
    for i in range(1, N):
        tmp = len(set(S[:i]) & set(S[i:]))
        if ans < tmp:
            ans = tmp

    print(ans)
    return


if __name__ == '__main__':
    main()
