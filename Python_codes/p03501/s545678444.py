#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

input = sys.stdin.readline

def main():
    N, A, B = map(int, input().split())
    print(min(A*N, B))

main()
