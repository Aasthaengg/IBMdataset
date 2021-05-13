#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()
r = 'Bad'
if s[0] != s[1] and s[1] != s[2] and s[2] != s[3]:
  r = 'Good'
print(r)
