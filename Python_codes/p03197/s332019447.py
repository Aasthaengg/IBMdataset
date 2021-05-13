#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    N = int(input())
    l = [int(input()) for _ in range(N)]

    if sum(l)%2==1:
        print('first')
    else:
        ret = 'second'
        for i in l:
            if i%2!=0:
                ret = 'first'
                break
        print(ret)

if __name__ == '__main__':
    main()