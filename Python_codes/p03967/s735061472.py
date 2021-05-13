#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    S = list(input())
    ret = 0
    for i, a in enumerate(S):
        if i%2==0:
            #jibunnha g
            if a=='p':
                ret -= 1
        else:
            if a=='g':
                ret += 1
    print(ret)

if __name__ == '__main__':
    main()