# -*- coding: utf-8 -*-

def main():

    X = int(input())

    num = 100
    ans = 0

    while num < X:
        num += + num // 100
        ans += 1

    print(ans)


if __name__ == "__main__":
    main()