#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    A, B, C = map(int, input().split())
    ret = 1 + min(A+B, C-1) + B

    print(ret)

if __name__ == '__main__':
    main()