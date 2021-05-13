# -*- coding: utf-8 -*-

n = int(raw_input())
A = {0}
for c in raw_input().split():
    for i in A.copy():
        A.add(i+int(c))
q = int(raw_input())
M = map(int, raw_input().split())
for m in M:
    if m in A:
        print "yes"
    else:
        print "no"