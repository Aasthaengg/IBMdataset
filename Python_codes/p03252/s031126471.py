#!/usr/bin/env python3

from collections import defaultdict

def II(): return int(input())
def MII(): return map(int, input().split())
def LII(): return list(map(int, input().split()))

def main():
    S = input()
    T = input()

    s1 = {}
    t1 = {}

    for i, (s, t) in enumerate(zip(S, T)):
        if s in s1 and t in t1:
            if s1[s] != t1[t]:
                print('No')
                return
        elif s not in s1 and t not in t1:
            s1[s] = i
            t1[t] = i
        else:
            print('No')
            return
    
    print('Yes')


if __name__ == '__main__':
    main()
