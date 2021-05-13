#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    h, w, a, b = map(int, input().split())
    for i in range(b):
        print('1'*a + '0'*(w-a))
    for i in range(h-b):
        print('0'*a + '1'*(w-a))

if __name__ == '__main__':
    main()