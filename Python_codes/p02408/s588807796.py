# -*- coding: utf-8 -*-

dic = {}
pat = ['S', 'H', 'C', 'D']
rank = [k for k in range(1, 14)]

#   dic?????????
for p in pat:
    for r in rank:
        dic[(p, r)] = 0

n = input()
for i in range(n):
    l = map(str, raw_input().split())
    p = l[0]
    r = int(l[1])
    dic[(p, r)] += 1

for p in pat:
    for r in rank:
        if dic[(p, r)] == 0:
            print "%s %d" %(p, r)