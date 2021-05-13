#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    X, Y = map(int, input().split())
    ret = 1
    tmp = X
    while Y>=tmp:
        if tmp*2>Y:
            break
        else:
            tmp = tmp * 2
            ret += 1

    print(ret)

if __name__ == '__main__':
    main()