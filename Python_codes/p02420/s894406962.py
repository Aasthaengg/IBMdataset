#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
?????????????????£?????????
"""

while True:
    cards = input().strip()
    if cards == "-":
        break
    times = int(input().strip())
    for i in range(times):
        num = int(input().strip())
        cards = cards[num:] + cards[:num]
    print(cards)