from collections import deque

# 双方向連結リストの実装
N = int(input())
commands = [input() for _ in range(N)]

d = deque()

for c in commands:
    if c == "deleteFirst":
        if d:
            d.popleft()

    elif c == 'deleteLast':
        if d:
            d.pop()

    elif 'delete ' in c:
        _, key = c.split()
        key = int(key)
        if key in d:
            d.remove(key)

    elif 'insert ' in c:
        _, key = c.split()
        key = int(key)
        d.appendleft(key)

print(*d)

