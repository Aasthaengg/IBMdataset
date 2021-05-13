import sys

input = sys.stdin.readline


def main():
    a, b = map(int, input().split())

    x = (a + b) / 2
    if x.is_integer():
        ans = int(x)
    else:
        ans = int(x) + 1

    print(ans)


if __name__ == "__main__":
    main()
