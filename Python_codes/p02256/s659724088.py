# -*- coding: utf-8 -*-


def converter(a, b):
    if a == 0:
        return b
    else:
        return converter(b % a, a)


def main():
    a, b = sorted([int(x) for x in raw_input().strip().split(' ')])
    print converter(a, b) 


if __name__ == '__main__':
    main()