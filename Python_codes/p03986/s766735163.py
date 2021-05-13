#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    S = input()
    cnt = 0
    ret = len(S)
    for a in S:
        if a == 'S':
            cnt += 1
        else:
            if cnt>0:
                cnt-=1
                ret-=2
    print(ret)

if __name__ == '__main__':
    main()