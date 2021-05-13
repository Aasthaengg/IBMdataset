# -*- coding: utf-8 -*-

H, W = map(int, input().split())

l = []

l.append('#' * (W + 2))

for i in range(H):
    s = str(input())
    l.append('#' + s + '#')

l.append('#' * (W + 2))

print(*l, sep='\n')