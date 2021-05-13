import sys

input = sys.stdin.readline


def main():
    x1, y1, x2, y2 = map(int, input().split())

    delta_x = x2 - x1
    delta_y = y2 - y1
    x3, y3 = x2 - delta_y, y2 + delta_x
    x4, y4 = x3 - delta_x, y3 - delta_y

    print(x3, y3, x4, y4)


if __name__ == "__main__":
    main()
