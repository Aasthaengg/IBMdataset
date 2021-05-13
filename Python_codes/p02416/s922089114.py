#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
????????????
"""
while True:
    cnt = 0
    inp = input().strip()
    if int(inp[0]) == 0:
        break
    for i in range(len(inp)):
        cnt += int(inp[i])
    print(cnt)