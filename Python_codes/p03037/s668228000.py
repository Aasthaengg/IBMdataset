# -*- coding: utf-8 -*-
import numpy as np
n, m = map(int, input().split())


cards = np.zeros(n+1, dtype=int)

for _ in range(m):
    l,r = map(int, input().split())
    cards[l-1] += 1
    cards[r] -= 1

cum = cards.cumsum()

print(len(cum[cum==m]))
