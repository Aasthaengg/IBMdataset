import sys

input = sys.stdin.readline


def main():
    S = input().rstrip()

    if all(s in S for s in "abc"):
        ans = "Yes"
    else:
        ans = "No"

    print(ans)


if __name__ == "__main__":
    main()
