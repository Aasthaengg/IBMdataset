import sys

input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    ans = K * (K - 1)**(N - 1)
    print(ans)


if __name__ == "__main__":
    main()
