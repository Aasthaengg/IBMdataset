#!/bin/env python
# coding: utf-8

import sys

def main():
    A, B, C = sys.stdin.readline().strip().split()
    if A == B and B == C:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
