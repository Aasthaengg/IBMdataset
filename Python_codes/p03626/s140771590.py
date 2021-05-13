import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())
    S1 = readline().strip()
    S2 = readline().strip()

    if S1[0] == S2[0]:
        ans = 3
        i = 1
    else:
        ans = 6
        i = 2

    while i < N:
        if S1[i] == S2[i]:
            if S1[i - 1] == S2[i - 1]:
                ans = ans * 2 % MOD
            i += 1
        else:
            if S1[i - 1] == S2[i - 1]:
                ans = ans * 2 % MOD
            else:
                ans = ans * 3 % MOD
            i += 2

    print(ans)
    return


if __name__ == '__main__':
    main()
