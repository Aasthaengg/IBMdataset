import sys
from collections import deque
n = int(sys.stdin.readline())

ans = deque()

for i in range(n):
    c = sys.stdin.readline()[:-1]
    if c[0] == 'i':
        ans.appendleft(c[7:])
    elif c[6] == ' ':
        try:
            ans.remove(c[7:])
        except:
            pass
    elif c[6] == 'F':
        ans.popleft()
    else:
        ans.pop()

print(' '.join(ans))