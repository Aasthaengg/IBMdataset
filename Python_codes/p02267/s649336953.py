# -*- coding: utf-8 -*-

n = int(raw_input())
S = map(int, raw_input().split())
q = int(raw_input())
T = map(int, raw_input().split())
count = 0
for i in range(q):
    for j in range(n):
        if T[i] == S[j]:
            count += 1
            break
print count