#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    K, T = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    x=A[0]
    print(max(x-1-(K-x),0))

if __name__ == '__main__':
    main()