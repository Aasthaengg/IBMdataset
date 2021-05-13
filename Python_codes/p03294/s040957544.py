import sys

input = sys.stdin.readline


def main():
    N = int(input())
    a = list(map(int, input().split()))

    ans = sum(a) - N
    print(ans)


if __name__ == "__main__":
    main()
