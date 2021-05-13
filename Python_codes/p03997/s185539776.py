# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
def input(): return sys.stdin.readline().rstrip()

def main():
    a=int(input())
    b=int(input())
    h=int(input())
    print((a+b)*h//2)

if __name__ == '__main__':
    main()
