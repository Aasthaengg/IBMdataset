import sys

input = sys.stdin.readline


def main():
    N = int(input())

    for i in range(1, 10):
        if N <= 111 * i:
            ans = 111 * i
            break

    print(ans)


if __name__ == "__main__":
    main()
