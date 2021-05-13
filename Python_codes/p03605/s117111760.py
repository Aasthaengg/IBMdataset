import sys

input = sys.stdin.readline


def main():
    N = int(input())

    if "9" in str(N):
        ans = "Yes"
    else:
        ans = "No"

    print(ans)


if __name__ == "__main__":
    main()
