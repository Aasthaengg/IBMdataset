#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    A, B, C = map(int, input().split())
    print(sum(sorted([A, B, C])[:2]))


if __name__ == "__main__":
    main()
