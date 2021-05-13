# -*- coding: utf-8 -*-
n, p = map(int, input().split())
s = input()

if p == 2:
    ret = 0
    for i in range(len(s)):
        if int(s[i]) % 2 == 0:
            ret = ret + i + 1
    print(ret)
elif p == 5:
    ret = 0
    for i in range(len(s)):
        if int(s[i]) % 5 == 0:
            ret = ret + i + 1
    print(ret)
else:
    c_list = [0] * n
    power = 1
    for i in range(len(s)):
        c_list[i] = (c_list[i-1] + (int(s[-i-1]) * power)) % p
        power *= 10
        power = power % p
    c_list.append(0)
    counter = [0] * p
    for i in c_list:
        counter[i] += 1
    ret = 0
    for item in counter:
        if item >= 2:
            ret = ret + (item * (item - 1) // 2)
    print(ret)
