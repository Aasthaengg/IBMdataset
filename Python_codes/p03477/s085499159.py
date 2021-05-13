import sys

input = sys.stdin.readline


def main():
    A, B, C, D = map(int, input().split())

    if A + B > C + D:
        ans = "Left"
    elif A + B == C + D:
        ans = "Balanced"
    else:
        ans = "Right"

    print(ans)


if __name__ == "__main__":
    main()
