import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    S = readline().strip()

    ans = INF
    for i in range(len(S) - 3 + 1):
        ans = min(ans, abs(int(S[i : i + 3]) - 753))

    print(ans)
    return


if __name__ == '__main__':
    main()
