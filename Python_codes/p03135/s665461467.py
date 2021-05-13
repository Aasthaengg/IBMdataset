import sys

input = sys.stdin.readline


def main():
    T, X = map(int, input().split())
    ans = T / X
    print(ans)


if __name__ == "__main__":
    main()
