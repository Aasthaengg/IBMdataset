#!/usr/bin python3
# -*- coding: utf-8 -*-

from collections import Counter
def main():
    A = input()
    n = len(A)
    A = Counter(A)
    ret = n *(n-1)//2
    for i, c in A.items():
        ret -= c*(c-1)//2
    print(ret+1)

if __name__ == '__main__':
    main()