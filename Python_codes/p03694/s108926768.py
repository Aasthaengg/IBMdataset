# -*- coding: utf-8 -*-
input()
pos = sorted(list(map(int, input().split())))
print(max(pos) - min(pos))