# -*- coding: utf-8 -*-

n, a, b = map(int, input().split())

max_r = min([a,b])
min_r = max([0, (a+b)-n])

print("{} {}".format(max_r, min_r))
