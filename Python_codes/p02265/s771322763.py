# coding: utf-8

import sys
from collections import deque

n = int(input())

task_name = (
    "insert",
    "delete",
    "deleteFirst",
    "deleteLast",
)

a = deque()

for task in map(lambda x: [x] if x in task_name else x.split(), sys.stdin.readlines()):
    #deleteFirst,deleteLast
    if len(task) == 1:
        if task[0] == "deleteFirst":
            a.popleft()
        else:
            a.pop()

    #insert,delete
    else:
        if task[0] == "insert":
            a.appendleft(task[1])
        elif task[1] in a:
            a.remove(task[1])

print(*a)