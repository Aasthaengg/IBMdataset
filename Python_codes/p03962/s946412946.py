# -*- coding: utf-8 -*-
a,b,c = map(int, input().split())
cnt = 0
if a != b:
  cnt += 1
if a != c:
  cnt += 1
if b != c:
  cnt += 1
if a==c and b==c:
  cnt += 1
print(int(cnt))