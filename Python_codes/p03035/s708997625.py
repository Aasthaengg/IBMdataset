# -*- coding: utf-8 -*-

def main():

    A, B = map(int, input().split())

    if A >= 13:
        ans = B

    elif 6 <= A <= 12:
        ans = B / 2

    elif A <= 5:
        ans = 0

    print(int(ans))


if __name__ == "__main__":
    main()