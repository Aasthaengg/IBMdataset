#!/usr/bin/env python3

N, A, B, C, D = map(int, input().split())
S = input()

#hunuke

h = S[A-1:D+1].count('##')
m3 = S[B-2:D+1].count('...')

if C < D:
    if h == 0: print('Yes')
    else: print('No')
else:
    if m3 != 0 and h == 0:
        print('Yes')
    else: print('No')
    
