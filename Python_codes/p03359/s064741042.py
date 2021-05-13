import sys

input = sys.stdin.readline


def main():
    a, b = map(int, input().split())

    ans = a - 1
    ans += 1 if a <= b else 0
    print(ans)


if __name__ == "__main__":
    main()
