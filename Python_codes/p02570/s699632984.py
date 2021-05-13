#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    D, T, S = map(int, input().split())
    print("No" if T * S < D else "Yes")


if __name__ == "__main__":
    main()
