#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    S = int(input())
    y = (S+10**9-1)//(10**9)
    x = y*(10**9)-S
    print(' '.join(map(str,[0,0,10**9,1,x,y])))

if __name__ == '__main__':
    main()