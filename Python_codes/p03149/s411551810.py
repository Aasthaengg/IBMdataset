import sys

input = sys.stdin.readline


def main():
    N = list(map(int, input().split()))

    if (1 in N) and (9 in N) and (7 in N) and (4 in N):
        ans = "YES"
    else:
        ans = "NO"

    print(ans)


if __name__ == "__main__":
    main()
