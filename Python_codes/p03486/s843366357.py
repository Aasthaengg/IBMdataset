#!/usr/bin/env python3

S = sorted(list(input()))
T = sorted(list(input()))[::-1]

if ''.join(S) < ''.join(T):
    print('Yes')
else:
    print('No')
