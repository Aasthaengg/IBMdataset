import sys
from collections import deque

n = int(input())
ary = deque([])

for line in sys.stdin:
    op = line.strip().split()
    cmd = op[0]

    if cmd == 'insert':
        x = op[1]
        ary.appendleft(x)

    elif cmd == 'delete':
        x = op[1]
        if x in ary:
            ary.remove(x)

    elif cmd == 'deleteLast':
        ary.pop()

    else:
        ary.popleft()

print(*ary)

