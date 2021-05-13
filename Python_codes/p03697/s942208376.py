#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    A, B = map(int, input().split())
    print('error'if (A + B) >= 10 else (A + B))


if __name__ == "__main__":
    main()
