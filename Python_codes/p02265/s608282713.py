#  deque

import collections
import sys
deque = collections.deque([])

n = int(input())
for i in range(n):
    query = sys.stdin.readline().split()
    if query[0] == "insert":
        deque.appendleft(int(query[1]))
    elif query[0] == "deleteFirst":
        deque.popleft()
    elif query[0] == "deleteLast":
        deque.pop()
    elif query[0] == "delete":
        try:
            deque.index(int(query[1]))
        except:
            pass
        else:
            deque.remove(int(query[1]))

print(*deque)
