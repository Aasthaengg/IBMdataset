#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    S = input()

    ret = 0
    cntW = 0
    cntB = 0
    for i, si in enumerate(S):
        #cntW,cntB
        if si=='W':
            cntW+=1
            ret+=cntB
        else:
            cntB+=1

    print(ret)

if __name__ == '__main__':
    main()