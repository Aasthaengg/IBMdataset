import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)

MOD = 10 ** 9 + 7
INF = float("inf")


def main():
    N = int(input())
    A = list(map(int, input().split()))
    answer = 0
    for i in range(N):
        if i % 2 == 0 and A[i] % 2 == 1:
            answer += 1
    print(answer)


if __name__ == "__main__":
    main()
