import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)

MOD = 10 ** 9 + 7
INF = float("inf")


def main():
    N = int(input())
    answer = 0

    for i in range(1, N + 1):
        num = N // i
        answer += ((num * i) + i) * num // 2
    print(answer)


if __name__ == "__main__":
    main()
