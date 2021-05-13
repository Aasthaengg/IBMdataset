# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))
s = 0
for a in A:
  s ^= a
ans = list()
for a in A:
  ans.append(s ^ a)
print(" ".join(map(str, ans)))