import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    S = readline().strip()
    K = int(readline())

    subs = set()

    for i in range(len(S)):
        for j in range(i + 1, min(len(S) + 1, i + K + 1)):
            subs.add(S[i:j])

    subs = sorted(subs)
    print(subs[K - 1])

    return


if __name__ == '__main__':
    main()
