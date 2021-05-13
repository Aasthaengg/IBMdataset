#!/usr/bin/env python3

def main():
    N, D = map(int, open(0).read().split())

    print(-(-N//(2*D + 1)))


main()