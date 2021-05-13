# -*- coding: utf-8 -*-

X = int(input())

num = X // 100
if num*100 <= X and X<=num*105:
    print("1")
else:
    print("0")
