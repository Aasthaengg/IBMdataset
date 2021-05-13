#!/usr/bin/env python3
*a, k = map(int, open(0).read().split())
if max(a) - min(a) <= k:
    print('Yay!')
else:
    print(':(')
