import sys

input = sys.stdin.readline


def main():
    N = int(input())

    num = str(N)
    ans = "No"
    if num[0] == num[1] == num[2]:
        ans = "Yes"
    if num[1] == num[2] == num[3]:
        ans = "Yes"

    print(ans)


if __name__ == "__main__":
    main()
