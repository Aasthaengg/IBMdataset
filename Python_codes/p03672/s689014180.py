import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    S = readline().strip()
    N = len(S)

    for w in range(N // 2 - 1, 0, -1):
        ok = True
        for i in range(w):
            if S[i] != S[i + w]:
                ok = False
                break
        if ok:
            print(2 * w)
            return

    return


if __name__ == '__main__':
    main()
