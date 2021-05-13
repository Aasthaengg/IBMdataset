import sys

input = sys.stdin.readline


def main():
    R = int(input())

    if R < 1200:
        ans = "ABC"
    elif R < 2800:
        ans = "ARC"
    else:
        ans = "AGC"

    print(ans)


if __name__ == "__main__":
    main()
