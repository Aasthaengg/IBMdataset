# coding=utf-8
from collections import deque
n = int(input())
deque = deque()

for i in range(n):
    inp = list(input().split())
    if inp[0] == 'deleteFirst':
        deque.popleft()
    elif inp[0] == 'deleteLast':
        deque.pop()
    elif inp[0] == 'insert':
        deque.appendleft(inp[1])
    else:
        if inp[1] in deque:
            deque.remove(inp[1])

print(*deque)