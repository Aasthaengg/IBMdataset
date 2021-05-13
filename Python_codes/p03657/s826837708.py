#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    A, B = map(int, input().split())
    print('Possible' if any([A % 3 == 0,
                             B % 3 == 0,
                             (A + B) % 3 == 0]) else 'Impossible')


if __name__ == "__main__":
    main()
