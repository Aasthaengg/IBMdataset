# coding: utf-8

# 入力
indata = input()

# データ長
length = len(indata)

if length == 2:
    print(indata)
else:
    print(indata[::-1])

