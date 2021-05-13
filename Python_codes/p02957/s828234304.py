#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 問題：https://atcoder.jp/contests/abc135/tasks/abc135_a

a, b = map(int, input().strip().split())
diff = abs(a-b)
if diff % 2 == 0:
    print(int((a+b)/2))
else:
    print('IMPOSSIBLE')

