#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    S = input()
    S = S.replace('BC','Z')
    S = S.replace('B',' ')
    S = S.replace('C',' ')
    S = S[::-1]
    S = S.split()
    ret = 0
    for s in S:
        zcn = 0
        for si in s:
            zcn += (si == 'Z')
            ret += zcn * (si == 'A')
    print(ret)

if __name__ == '__main__':
    main()