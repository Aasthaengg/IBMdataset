#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys

def main():
    input = sys.stdin.readline
    a,b = map(int, input().split())
    if a <= 8 and b <= 8:
        print("Yay!")
    else:
        print(":(")




if __name__=="__main__":
    main()
