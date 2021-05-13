#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    N = int(input())
    ret = 10**9
    for a in range(1,N):
        b = N-a
        ret = min(ret,sum(map(int,list(str(a))))+sum(map(int,list(str(b)))))

    print(ret)

if __name__ == '__main__':
    main()