import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def main():
    N = int(input())
    A = sorted(list(map(int, input().split())), reverse=True)

    # print(A)

    ans = 0

    for i in range(1, 2 * N, 2):
        ans += A[i]

    # for i in range(N):
    #     ans += A[i + N]

    print(ans)


if __name__ == "__main__":
    main()
