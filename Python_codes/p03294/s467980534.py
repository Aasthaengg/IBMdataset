#!/usr/bin/env python3

def main():
    N, *a = map(int, open(0).read().split())

    print(sum(a) - N)


main()