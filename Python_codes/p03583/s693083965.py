#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    N = int(input())
    for x in range(1,3501):
        for y in range(x,3501):
            bunshi = x*y*N
            bunbo  = 4*x*y-(x+y)*N
            if bunbo>0 and bunshi%bunbo==0:
                print(x,y,bunshi//bunbo)
                exit()

if __name__ == '__main__':
    main()