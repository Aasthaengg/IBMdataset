#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    A, B, C, D = map(int, input().split())
    print(max(A * B, C * D))


if __name__ == "__main__":
    main()
