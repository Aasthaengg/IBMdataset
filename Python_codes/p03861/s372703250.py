# -*- coding: utf-8 -*-

def main():

    a, b, x = map(int, input().split())
    ans = 0

    ans = (b // x) - ((a-1) // x)

    print(ans)


if __name__ == "__main__":
    main()