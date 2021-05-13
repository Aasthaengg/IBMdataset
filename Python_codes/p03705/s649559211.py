#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    N, A, B = map(int, input().split())
    if N == 1 and A>B:
        print(0)
    else:
        mn=B+A*(N-1)
        mx=A+B*(N-1)
        print(max(mx-mn+1,0))

if __name__ == '__main__':
    main()