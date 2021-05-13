import math


def main():
    # n = int(input())
    n, k = map(int, input().split())
    # h = list(map(int, input().split()))
    s = list(input())
    # h = [int(input()) for _ in rane(n)]

    s[k-1] = s[k-1].lower()
    print("".join(s))


if __name__ == '__main__':
    main()
