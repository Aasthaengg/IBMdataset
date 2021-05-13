import sys

input = sys.stdin.readline


def main():
    n = input().rstrip()

    ans = ""
    for s in n:
        if s == "1":
            ans += "9"
        else:
            ans += "1"

    print(ans)


if __name__ == "__main__":
    main()
