#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    L, R, d = map(int, input().split())
    l = list(range(L, R+1))
    cnt =0
    for i in l:
        if i%d==0:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()