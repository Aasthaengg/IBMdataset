# -*- coding: utf-8 -*-

n, k = map(int, input().split())
s = list(str(input()))

s[k - 1] = s[k - 1].lower()

print(*s, sep='')