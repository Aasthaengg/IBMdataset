import sys

input = sys.stdin.readline


def main():
    N = int(input())

    num = str(N)
    if num[0] == num[-1]:
        ans = "Yes"
    else:
        ans = "No"

    print(ans)


if __name__ == "__main__":
    main()
