#!/usr/bin/env python3

def main():
    N, R = map(int, open(0).read().split())
    
    if N >= 10:
        print(R)
    else:
        print(R + 100 * (10 - N))


main()