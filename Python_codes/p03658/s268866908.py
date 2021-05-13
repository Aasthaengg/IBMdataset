# -*- coding: utf-8 -*-
n, k = map(int,input().split())
l = [int(i) for i in input().split()]

l.sort()
print(sum(l[n - k:]))
