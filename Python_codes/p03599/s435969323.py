# -*- coding: utf-8 -*-
import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

A,B,C,D,E,F = map(int, readline().split())
ans = (100*A,0)
max_con = 0

for a in range(31):
    for b in range(31):
        for c in range(50):
            for d in range(50):
                W = a * 100 * A + b * 100 * B
                S = c*C + d*D
                SW = S + W 
                e = W // 100
                if F < SW or SW == 0:
                    continue
                if e * E < S:
                    continue
                tmp = 100 * S / SW
                if tmp > max_con:
                    max_con = tmp
                    ans = (SW,S)
print(' '.join(str(a) for a in ans))