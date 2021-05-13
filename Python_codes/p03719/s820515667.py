#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    A, B, C = map(int, input().split())
    print('Yes'if all([C >= A, C <= B]) else 'No')


if __name__ == "__main__":
    main()
