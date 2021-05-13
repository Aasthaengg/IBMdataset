#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

def main():
    X, Y = map(int, input().split())

    print(gcd(X,Y))

if __name__ == "__main__": main()