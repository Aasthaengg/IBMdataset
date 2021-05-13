# -*- coding: utf-8 -*-


def main():
    n, a, b = map(int, input().split())
    if n * a > b:
        print(b)
    elif n * a <= b:
        print(n * a)


if __name__ == '__main__':
    main()