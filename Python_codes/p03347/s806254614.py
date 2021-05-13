import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)

MOD = 10 ** 9 + 7
INF = float("inf")


def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]

    if A[0] != 0:
        print(-1)
        return
    answer = 0
    flag = 0
    for i in range(N - 1):
        if A[i + 1] - A[i] > 1:
            print(-1)
            return
        elif A[i + 1] == A[i]:
            answer += A[i]
        elif A[i + 1] == A[i] + 1:
            flag = A[i + 1]
        else:
            answer += flag
            flag = A[i + 1]
    answer += flag
    print(answer)


if __name__ == "__main__":
    main()
