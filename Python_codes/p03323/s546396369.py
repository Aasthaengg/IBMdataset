#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline().rstrip

A,B = map(int, input().split())

ans = ":(" if A > 8 or B > 8 else "Yay!"
print(ans)

