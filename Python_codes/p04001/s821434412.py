#!/usr/bin/env python3
# 入力
s = input()
num = len(s)-1
ret = 0

for i in range(2**num):
    st = 0
    for j in range(num):
        if (i >> j) & 1:
            ret += int(s[st:j+1])
            st = j+1
    ret += int(s[st:])

print(ret)



