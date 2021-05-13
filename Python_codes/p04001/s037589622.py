#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    S = input()
    l = len(S)-1
    ret = 0
    for i in range(2**l):
        fs = S[0]
        for j in range(l):
            if (i>>j & 1) == 1:
                fs += '+'
            fs += S[j+1]
        ret += eval(fs)
    print(ret)

if __name__ == '__main__':
    main()