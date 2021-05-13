#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    N, H, W = map(int, input().strip().split())
    count = 0
    for _ in range(N):
        A, B = map(int, input().strip().split())
        if H <= A and W <= B:
            count += 1

    print(count)

if __name__ == "__main__":
    main()
