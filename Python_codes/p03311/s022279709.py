import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a - i - 1 for i, a in enumerate(A)]
    A.sort()
    i = N // 2
    b = A[i]
    ans = 0
    for a in A:
        ans += abs(a - b)
    print(ans)


if __name__ == "__main__":
    main()
