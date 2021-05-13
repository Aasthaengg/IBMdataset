#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    X, T = map(int, input().split())
    print(max(X - T, 0))


if __name__ == "__main__":
    main()
