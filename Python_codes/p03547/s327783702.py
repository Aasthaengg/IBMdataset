import sys

input = sys.stdin.readline


def main():
    X, Y = input().split()

    if X < Y:
        ans = "<"
    elif X > Y:
        ans = ">"
    else:
        ans = "="

    print(ans)


if __name__ == "__main__":
    main()
