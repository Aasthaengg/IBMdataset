# -*- coding: utf-8 -*-

import sys
import os


for s in sys.stdin:
    sentence = s.strip()
    if sentence == '-':
        break

    N = int(input())
    for i in range(N):
        h = int(input())
        sentence = sentence[h:] + sentence[:h]
    print(sentence)