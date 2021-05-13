# coding: utf-8
from collections import deque

inputs = deque(raw_input().split())
q = deque()
while len(inputs):
    op = inputs.popleft()
    if op == '+':
        q.append(q.pop() + q.pop())
    elif op == '-':
        v1 = q.pop()
        v2 = q.pop()
        q.append(v2 - v1)
    elif op == '*':
        q.append(q.pop() * q.pop())
    else:
        q.append(int(op))

print q.pop()

