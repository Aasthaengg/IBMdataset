#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    A, B = map(int, input().split())
    print(A if A <= B else A - 1)


if __name__ == "__main__":
    main()
