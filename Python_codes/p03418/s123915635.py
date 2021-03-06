import sys


def input():
    return sys.stdin.readline().strip()


def main():
    N, K = map(int, input().split())
    answer = 0
    for b in range(1, N + 1):
        p = N // b
        q = N % b
        answer += p * max(0, b - K)
        answer += max(0, q - K + 1)
    if K == 0:
        answer -= N
    print(answer)


if __name__ == "__main__":
    main()
