#!/usr/bin/env python3
import sys
from collections import Counter

def main():
    N = int(input())
    S = input()
    L = Counter(S)
    p = 10**9 + 7
    ans = 1
    for l in L.items():
        ans =  ans * (l[1] + 1) % p
    print((ans - 1) % p)

if __name__ == '__main__':
    main()
