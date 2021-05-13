#!/usr/bin/env python3

import sys

def debug(*a):
    print(*a, file=sys.stderr)

s = input().strip()
v = [int(s[i]) for i in range(4)]
for x in range(8):
    a = v[0]
    for i in range(3):
        if (x >> i) & 1:
            a += v[i+1]
        else:
            a -= v[i+1]
    debug(f'x = {x}, a = {a}')
    if a == 7:
        s = ''
        for i in range(3):
            s += str(v[i])
            if (x >> i) & 1:
                s += '+'
            else:
                s += '-'
        s += str(v[3]) + '=7'
        print(s)
        sys.exit(0)
        
