import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N = int(input())
    S1 = input()
    S2 = input()
    # 縦
    if S1[0] == S2[0]:
        ans = 3

        # 1は縦，0は横
        prev = 1
    else:
        ans = 3 * 2
        prev = 0

    for i in range(1, N):
        # 1つ前が横
        if prev == 0:
            # 縦
            if S1[i] == S2[i]:
                prev = 1
                continue
            else:
                # 同じドミノ
                if S1[i - 1] == S1[i]:
                    continue
                # 違うドミノ
                else:
                    ans *= 3
                    ans %= MOD
        else:
            # 一つ前が縦
            # 縦
            if S1[i] == S2[i]:
                ans *= 2
                ans %= MOD
            else:
                prev = 0
                ans *= 2
                ans %= MOD

    print(ans)


if __name__ == "__main__":
    main()
