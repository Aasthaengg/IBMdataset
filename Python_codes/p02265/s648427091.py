from collections import deque
from sys import stdin
n = int(input())
L = deque()
for _ in range(n):
    com = list(map(str, stdin.readline().split()))
    if com[0] == 'insert':
        i = int(com[1])
        L.appendleft(i)
    elif com[0] == 'delete':
        i = int(com[1])
        try:
            L.remove(i)
        except ValueError:
            continue
    elif com[0] == 'deleteFirst':
        L.popleft()
    elif com[0] == 'deleteLast':
        L.pop()
for i in range(len(L)):
    if i == len(L) - 1:
        print(L[i])
    else:
        print(L[i], end=' ')
