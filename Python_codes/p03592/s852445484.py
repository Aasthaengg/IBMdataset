import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N, M, K = [int(x) for x in input().split()]

    for i in range(N + 1):
        for j in range(M + 1):
            if M * i + (N - i) * j - i * j == K:
                print("Yes")
                return

    print("No")

if __name__ == '__main__':
    main()
