import sys

input = sys.stdin.readline


def main():
    x, y = map(int, input().split())

    X = abs(x)
    Y = abs(y)
    d = abs(X - Y)
    if x >= 0 and y >= 0 and X > Y:
        ans = min(1 + d + 1, 1 + (x + y))
    elif x >= 0 and y >= 0:
        ans = d
    elif x >= 0 and y <= 0 and X > Y:
        ans = 1 + d
    elif x >= 0 and y <= 0:
        ans = d + 1
    elif x <= 0 and y >= 0 and X > Y:
        ans = min(d + 1, y - x)
    elif x <= 0 and y >= 0:
        ans = min(1 + d, y - x)
    elif x <= 0 and y <= 0 and X > Y:
        ans = d
    elif x <= 0 and y <= 0:
        ans = 1 + d + 1

    print(ans)


if __name__ == "__main__":
    main()
