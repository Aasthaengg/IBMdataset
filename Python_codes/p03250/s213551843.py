# -*- coding: utf-8 -*-

s = sorted(list(map(int, input().split())), reverse=True)

print(eval("{}{} + {}".format(s[0], s[1], s[2])))