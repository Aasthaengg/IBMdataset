import sys

input = sys.stdin.readline


def main():
    D = int(input())

    if D == 25:
        ans = "Christmas"
    elif D == 24:
        ans = "Christmas Eve"
    elif D == 23:
        ans = "Christmas Eve Eve"
    else:
        ans = "Christmas Eve Eve Eve"

    print(ans)


if __name__ == "__main__":
    main()
