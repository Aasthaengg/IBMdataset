# -*- coding: utf-8 -*-

# 文字列の入力
s = raw_input()

# 整数の入力
a = int(raw_input())

r=list(s)[::a]
print ''.join(r)
