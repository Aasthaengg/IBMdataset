#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()
t = input()
r=0
for i in range(0,3):
  if s[i]==t[i]:
    r=r+1
print(r)