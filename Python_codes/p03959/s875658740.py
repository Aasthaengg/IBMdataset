import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N = int(input())
    T = list(map(int, input().split()))
    A = list(map(int, input().split()))

    if T[-1] != A[0]:
        print(0)
        return

    # 左からみていく
    ans = 1
    for i in range(1, N - 1):
        if T[i - 1] < T[i] and A[i] > A[i + 1]:
            if T[i] == A[i]:
                continue
            else:
                print(0)
                return
        elif A[i] > A[i + 1]:
            if A[i] > T[i]:
                print(0)
                return
        elif T[i - 1] < T[i]:
            if T[i] > A[i]:
                print(0)
                return
        else:
            m = min(A[i], T[i])
            ans *= m
            ans %= MOD

    print(ans)


if __name__ == "__main__":
    main()
