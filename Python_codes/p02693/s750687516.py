# -*- coding: utf-8 -*-

k = int(input())
a, b = map(int, input().split())

# b以下の最大のKの倍数を求める
largest = (b // k) * k # 切り捨ての商をk倍することで、最大のkの倍数が求められる
if largest >= a:
    print('OK')
else:
    print('NG')