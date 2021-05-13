#!/usr/bin/env python3
import itertools
N = int(input())
Name = {'M':0, 'A':0, 'R':0, 'C':0, 'H':0}


for i in range(N):
    S = input()
    if S[0] in Name: Name[S[0]] += 1

l = []
for k, v in Name.items():
    l.append(v)

ret = 0

for x in itertools.combinations(l, 3):
    ret += x[0]*x[1]*x[2]

print(ret)
