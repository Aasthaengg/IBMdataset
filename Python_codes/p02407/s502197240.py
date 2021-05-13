# -*- coding:utf-8 -*-
n = input()
a = [int(s) for s in input().split()]
a.reverse()
print(' '.join(map(str,a)))