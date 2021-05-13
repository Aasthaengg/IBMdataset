import sys

input = sys.stdin.readline


def main():
    N = int(input())
    K = int(input())

    ans = 1
    for _ in range(N):
        if 2 * ans < ans + K:
            ans *= 2
        else:
            ans += K

    print(ans)


if __name__ == "__main__":
    main()
