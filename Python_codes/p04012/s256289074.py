# -*- coding: utf-8 -*-

w = list(str(input()))
w_s = set(w)

for x in w_s:
    if w.count(x) % 2 != 0:
        print('No')
        exit()

print('Yes')