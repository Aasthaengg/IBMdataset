import sys

input = sys.stdin.readline


def main():
    X, A, B = map(int, input().split())

    if B <= A:
        ans = "delicious"
    elif B <= A + X:
        ans = "safe"
    else:
        ans = "dangerous"

    print(ans)


if __name__ == "__main__":
    main()
