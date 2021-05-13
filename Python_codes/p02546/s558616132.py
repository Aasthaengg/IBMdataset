#!/usr/bin/env python3


def main():
    a = input()
    if a[-1] == 's':
        print(a + 'es')
    else:
        print(a + 's')


if __name__ == '__main__':
    main()