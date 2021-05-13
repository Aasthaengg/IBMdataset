
#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

def int_mtx(N):
    x = []
    for _ in range(N):
        x.append(input())
    return x

N = int(input())
S = input()

ans = 0

for i in range(1,N-1):
    set1 = set(list(S[0:i]))
    set2 = set(list(S[i:N]))
    ans = max(ans,len(set1&set2))

print(ans)