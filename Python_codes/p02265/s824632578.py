from collections import deque
import sys

n = int(input())
result = deque()
func = {'insert':result.appendleft,\
        'delete':result.remove,\
        'deleteFirst':result.popleft,\
        'deleteLast':result.pop}

for line in sys.stdin.readlines():
    c = line.split()
    if len(c) > 1:
        try:
            func[c[0]](int(c[1]))
        except:
            continue
    else:
        func[c[0]]()

print(*result)

