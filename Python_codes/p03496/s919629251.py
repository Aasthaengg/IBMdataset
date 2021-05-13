#!/usr/bin/env python
# coding: utf-8

import fractions

def ri():
    return int(input())

def rl():
    return list(input().split())

def rli():
    return list(map(int, input().split()))

def main():
    n = ri()
    la = rli()
    checkpoints = [0]
    cur = la[0]
    for i in range(1, n):
        if la[i] >= cur:
            cur = la[i]
            continue
        if la[i] + cur*2 >= cur:
            cur = la[i] + cur*2
            continue
        checkpoints.append(i)
        cur = la[i]
    # print(checkpoints)
    ll = checkpoints[-1]
    op = []
    for c in checkpoints[::-1]:
        if c > ll:
            continue
        l = c
        cur = la[l]
        while l > 0:
            if la[l-1] <= cur:
                break
            op.append((l, l-1))
            op.append((l, l-1))
            cur = la[l-1] + cur * 2
            l -= 1
        ll = l-1
    cur = la[checkpoints[-1]]
    for i in range(checkpoints[-1], n-1):
        if la[i+1] >= cur:
            cur  = la[i+1]
        else:
            op.append((i, i+1))
            op.append((i, i+1))
            cur = la[i+1]+cur*2
    print(len(op))
    for o in op:
        print(o[0]+1, o[1]+1)



if __name__ == '__main__':
    main()
