#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
?????????????´¢
"""
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

inp = input().strip()
w = inp.translate(str.maketrans(upper,lower))
s = ""
while True:
    inp = input().strip()
    if inp == "END_OF_TEXT":
        break
    s = s + " " + inp.translate(str.maketrans(upper,lower))
arr = s.split()
print(arr.count(w))