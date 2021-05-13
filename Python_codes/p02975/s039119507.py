#!/usr/bin/env python3
import sys
from collections import Counter

def main():
    N = int(input())
    a = list(map(int, input().split()))
    l = Counter(a)
    if len(l)==1 and 0 in l:
        print('Yes')
        exit()
    if N%3==0 and len(l)==2 and 0 in l and l[0] == N//3:
        print('Yes')
        exit()
    if N%3==0 and len(l)==3:
        x,y,z = l.keys()
        if l[x] == l[y] == N//3 and x^y^z == 0:
            print('Yes')
            exit()
    print('No')

    

if __name__ == '__main__':
    main()
