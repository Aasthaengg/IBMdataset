#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    A, B, C = input().split()
    print('YES'if all([A[-1] == B[0], B[-1] == C[0]]) else 'NO')


if __name__ == "__main__":
    main()
