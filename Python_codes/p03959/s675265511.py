# -*- coding: utf-8 -*-
# get a integer
n = int(raw_input())

ls_t = map(int, raw_input().split())
ls_a = map(int, raw_input().split())

max_m1 = max(ls_t)
max_m2 = max(ls_a)

if max_m1 != max_m2 or ls_t.index(max_m1)  + list(reversed(ls_a)).index(max_m2) >= n or sorted(ls_t) != ls_t or sorted(ls_a) != list(reversed(ls_a)):
    print '0'
else:
    idx = ls_t.index(max_m1)
    def get_same_ls(ls):
        if len(ls) == 0:
            return []
        prev = ls[0]
        out = []
        for i in ls[1:]:
            if i == prev:
                out.append(i)
            else:
                prev = i
        return out
    ls_mult = get_same_ls(ls_t[:idx]) + get_same_ls(list(reversed(ls_a))[:n-idx-1])
    mult = 1
    m = pow(10, 9) + 7
    for i in ls_mult:
        mult = mult * i % m
    print mult
