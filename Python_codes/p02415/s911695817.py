#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
??§???????°?????????????
"""
tra = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
trb = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
inp = input().strip()
print(inp.translate(str.maketrans(tra,trb)))