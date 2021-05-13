import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


def main():
    MOD = 1000000007
    N, *A = map(int, read().split())

    ans = 1
    C = [0, 0, 0]
    for a in A:
        try:
            ans = (ans * C.count(a)) % MOD
            C[C.index(a)] += 1
        except ValueError:
            print(0)
            return

    print(ans)
    return


if __name__ == '__main__':
    main()
