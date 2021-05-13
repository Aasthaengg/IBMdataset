import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(10 ** 9)


MOD = 1000000007


def main():
    N = int(input())
    S1 = input()
    S2 = input()
    answer = 1
    cnt = 0
    while cnt < N:
        if cnt == 0:
            if S1[0] == S2[0]:
                answer *= 3
                cnt += 1
            else:
                answer *= 6
                cnt += 2
        else:
            if S1[cnt - 1] == S2[cnt - 1]:
                if S1[cnt] == S2[cnt]:
                    answer *= 2
                    cnt += 1
                else:
                    answer *= 2
                    cnt += 2
            else:
                if S1[cnt] == S2[cnt]:
                    answer *= 1
                    cnt += 1
                else:
                    answer *= 3
                    cnt += 2
        answer %= MOD

    print(answer % MOD)


if __name__ == "__main__":
    main()
