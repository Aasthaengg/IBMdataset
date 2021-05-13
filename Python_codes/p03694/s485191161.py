import sys

input = sys.stdin.readline


def main():
    N = int(input())
    a = list(map(int, input().split()))

    ans = max(a) - min(a)

    print(ans)


if __name__ == "__main__":
    main()
