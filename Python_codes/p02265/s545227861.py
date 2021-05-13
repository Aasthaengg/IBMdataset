# -*- coding: utf-8 -*-

import sys
import os
from collections import deque


N = int(input())
q = deque()

for i in range(N):
    lst = input().split()
    command = lst[0]
    if command == 'insert':
        v = int(lst[1])
        q.appendleft(v)
    elif command == 'delete':
        v = int(lst[1])
        try:
            q.remove(v)
        except Exception:
            pass
    elif command == 'deleteFirst':
        q.popleft()
    elif command == 'deleteLast':
        q.pop()

print(*q)