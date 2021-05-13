import sys

input = sys.stdin.readline


def main():
    N = int(input())
    A = list(map(int, input().split()))

    if sum(A) % 2 == 0:
        ans = "YES"
    else:
        ans = "NO"
    print(ans)


if __name__ == "__main__":
    main()
