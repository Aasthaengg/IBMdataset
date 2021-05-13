# -*- coding: utf-8 -*-

s = input()

c = s.find('C')
f = s.rfind('F')

print('Yes' if c != -1 and f != -1 and c < f else 'No')
