# -*- coding: utf-8 -*-
def pop_min_abs(l):
    abs_l = list(map(abs, l))
    l.pop(abs_l.index(min(abs_l)))
    return l



n, l = map(int, input().split())

apples = [l+i-1 for i in range(1,n+1)]
print(sum(pop_min_abs(apples)))
