import sys

input = sys.stdin.readline


def main():
    N = int(input())
    S = input().split()

    ans = "Four" if "Y" in S else "Three"

    print(ans)


if __name__ == "__main__":
    main()
