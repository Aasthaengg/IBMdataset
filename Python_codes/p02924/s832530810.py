#!/usr/bin/env python
# coding: utf-8

def ri():
    return int(input())

def rl():
    return list(input().split())

def rli():
    return list(map(int, input().split()))

def main():
    n = ri()
    print(((n-1)*n)//2)


if __name__ == '__main__':
    main()
