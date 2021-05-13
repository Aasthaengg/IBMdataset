# -*- coding: utf-8 -*-
# B - Narrow Rectangles Easy
# 標準入力の取得
W,a,b = list(map(int, input().split()))

# すでに連結しているかどうかで場合分け
is_connected = (a <= b + W) and (b <= a + W)
if is_connected:
    print(0)
else:
    print(min(abs(b-(a+W)), abs(a-(b+W))))