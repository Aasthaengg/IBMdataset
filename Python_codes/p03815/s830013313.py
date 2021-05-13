# -*- coding: utf -8 -*-
# C - X: Yet Another Die Game
# 標準入力の取得
x = int(input())

# yは6⇒5⇒6⇒5・・・とすればよいので、11で割った余りを場合分けすればよい
quotient = x // 11
remainder = x % 11
if remainder == 0:
    print(quotient * 2)
elif remainder <= 6:
    print(quotient * 2 + 1)
else:
    print(quotient * 2 + 2)