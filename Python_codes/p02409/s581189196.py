

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
??´?????????
"""

rooms = [[[0 for r in range(10)] for f in range(3)] for b in range(4)]

number = int(input())

for n in range(number):
    inp = input().split(" ")
    b = int(inp[0]) - 1
    f = int(inp[1]) - 1
    r = int(inp[2]) - 1
    v = int(inp[3])
    rooms[b][f][r] += v

for b in range(4):
    if b > 0:
        print("####################")
    for f in range(3):
        print(""," ".join(map(str,rooms[b][f])))