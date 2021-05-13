# -*- coding: utf-8 -*-

s = int(input())

h = int(s // (60 * 60))
s = s - h * (60 * 60)

m = int(s // 60)
s = s - m * 60

print('{0}:{1}:{2}'.format(h,m,s))