import sys

input = sys.stdin.readline


def main():
    r = int(input())
    g = int(input())
    # r + x = g * 2
    print(g * 2 - r)


if __name__ == "__main__":
    main()
