#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def is_right(a, b, c):
    a2 = a*a
    b2 = b*b
    c2 = c*c

    return a2==b2+c2 or b2==c2+a2 or c2==a2+b2

def main():
    N = int(input())

    for _ in range(N):
        a, b, c = map(int, input().split())

        result = is_right(a, b, c)
        print("YES" if result else "NO")

if __name__ == "__main__": main()