# -*- coding: utf-8 -*-


def main():
    k, x = map(int, input().split())

    ret = "No"
    if 500 * k >= x:
        ret = "Yes"
    return ret


if __name__ == '__main__':
    print(main())
