#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    A, B, C = map(int, input().split())
    ABC = sorted([A, B, C])
    print(ABC[2] if ABC[1] == ABC[0] else ABC[0])


if __name__ == "__main__":
    main()
