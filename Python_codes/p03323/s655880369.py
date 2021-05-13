import sys

input = sys.stdin.readline


def main():
    A, B = map(int, input().split())

    if A <= 8 and B <= 8:
        ans = "Yay!"
    else:
        ans = ":("

    print(ans)


if __name__ == "__main__":
    main()
