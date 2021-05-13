#!/usr/bin/env python3
# 整数の入力
s = input()
ret = 0
ret += s.count("+")
ret -= s.count("-")
 
print(ret)
