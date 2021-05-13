import math


def main():
    # n = int(input())
    # n, k = map(int, input().split())
    # h = list(map(int, input().split()))
    s = input()
    # h = [int(input()) for _ in rane(n)]
    f = int(s[:2])
    b = int(s[2:])
    if 1 <= f and f <= 12 and 1 <= b and b <= 12:
        print("AMBIGUOUS")
    elif 0 <= f and f <= 99 and 1 <= b and b <= 12:
        print("YYMM")
    elif 0 <= b and b <= 99 and 1 <= f and f <= 12:
        print("MMYY")
    else:
        print("NA")


if __name__ == '__main__':
    main()
