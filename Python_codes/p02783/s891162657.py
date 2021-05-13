#!/usr/bin/env python3
# -*- coding: utf-8 -*-
h,a = map(int, input().split())
r=h//a

if h-(r*a)!=0:
  r=r+1
print(r)
