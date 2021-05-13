#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

input = sys.stdin.readline

def main():
    A, B = map(int, input().split())
    print('error' if A + B >= 10 else A + B)

main()
