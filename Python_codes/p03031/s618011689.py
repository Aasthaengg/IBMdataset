# -*- coding: utf-8 -*-
import itertools

import numpy as np


# 読み込み
n, m = map(int, input().split())
swicthes = np.zeros((m, n), dtype=int)

for i in range(m):
    _, *s = map(lambda x: int(x) - 1, input().split())
    swicthes[i, np.array(s, dtype=int)] = 1

l = list(map(int, input().split()))
p = np.array(l, dtype=int)

# bit全探索
count = 0
for on in itertools.product([0, 1], repeat=n):
    _on = np.array(on, dtype=int)
    status = np.sum(swicthes * _on, axis=1) % 2
    if np.sum(p == status) == m:
        # 全ての電球が点灯している
        count += 1

print(count)
