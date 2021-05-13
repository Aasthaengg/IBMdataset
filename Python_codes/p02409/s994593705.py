# -*- coding: utf-8 -*-

dic = {}
bui = [k for k in range(1, 5)]
flo = [k for k in range(1, 4)]
roo = [k for k in range(1, 11)]

for b in bui:
    for f in flo:
        for r in roo:
            dic[(b, f, r)] = 0

n = input()
for i in range(n):
    list = map(int, raw_input().split())
    b = list[0]
    f = list[1]
    r = list[2]
    dic[(b, f, r)] += list[3]

for b in bui:
    for f in flo:
        buf = ""
        for r in roo:
            buf += " "+ str(dic[(b, f, r)])
        print buf
    if b < 4:
        print "#"*20