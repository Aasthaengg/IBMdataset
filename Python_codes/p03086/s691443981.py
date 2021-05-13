import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    S = readline().strip()

    ACGT = 'ACGT'

    ans = 0
    for i in range(len(S)):
        for j in range(i + 1, len(S) + 1):
            if j - i < ans:
                continue
            ok = True
            for c in S[i:j]:
                if c not in ACGT:
                    ok = False
                    break
            if ok and ans < j - i:
                ans = j - i

    print(ans)
    return


if __name__ == '__main__':
    main()
