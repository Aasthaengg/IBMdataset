#!/usr/bin/env python3

def main():
    A, B, C = map(int, open(0).read().split())
    if C - (A - B) >= 0:
        print(C - (A - B))
    else:
        print(0)


main()