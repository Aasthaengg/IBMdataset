#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    D, G = map(int, input().split())
    P = [0] * D
    C = [0] * D
    for i in range(D):
        p, c = map(int,input().split())
        P[i] = p
        C[i] = p * 100 * (i+1) + c

    ret = 1000
    for i in range(2 ** D):
        pt = 0
        ct = 0
        for j in range(D):
            if i >> j & 1:
                pt += C[j]
                ct += P[j]
            else:
                mxi = j
        for j in range(P[mxi]):
            if pt>=G:
                break
            else:
                pt += 100*(mxi+1)
                ct += 1
        if pt>=G:
            ret = min(ret, ct)
    print(ret)

if __name__ == '__main__':
    main()