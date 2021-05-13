import sys

input = sys.stdin.readline


def main():
    MOD = 1000000007
    N = int(input())
    S1 = input().strip()
    S2 = input().strip()

    ans = 1
    now = 0
    i = 0
    while i < N:
        if S1[i] != S2[i]:
            if now == 0:
                ans *= 6
            elif now == 1:
                ans *= 2
            else:
                ans *= 3
            now = 2
            i += 2
        else:
            if now == 0:
                ans *= 3
            elif now == 1:
                ans *= 2
            else:
                ans *= 1
            now = 1
            i += 1

    print(ans % MOD)


if __name__ == '__main__':
    main()
