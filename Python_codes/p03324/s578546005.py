#!/usr/bin/env python3

def main():
    D, N = map(int, open(0).read().split())
    if N == 100:
        print(101*100**D)
    else:
        print(N*100**D)


main()