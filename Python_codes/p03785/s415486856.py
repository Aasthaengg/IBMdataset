import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N, C, K = map(int, input().split())
    T = [int(input()) for _ in range(N)]
    T.sort()

    first = T[0]
    cnt = 1
    ans = 0
    for i in range(1, N):
        if cnt == C:
            ans += 1
            first = T[i]
            cnt = 1
        elif first + K < T[i]:
            ans += 1
            first = T[i]
            cnt = 1
        else:
            cnt += 1
    ans += 1

    print(ans)


if __name__ == "__main__":
    main()
