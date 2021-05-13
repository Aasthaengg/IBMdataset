# -*- coding: utf-8 -*-

import sys
import os
from queue import Queue


N, Q = list(map(int, input().split()))

q = Queue()
for i in range(N):
    lst = input().split()
    name = lst[0]
    t = int(lst[1])
    data = [name, t]
    q.put(data)

time = 0
while not q.empty():
    data = q.get()
    if data[1] > Q:
        data[1] -= Q
        q.put(data)
        time += Q
    else:
        time += data[1]
        print(data[0], time)