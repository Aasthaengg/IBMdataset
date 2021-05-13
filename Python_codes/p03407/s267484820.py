#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    A, B, C = map(int, input().split())
    print('Yes'if A + B >= C else 'No')


if __name__ == "__main__":
    main()
