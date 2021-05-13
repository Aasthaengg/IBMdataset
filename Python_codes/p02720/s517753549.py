import sys
from collections import deque
K = int(input())
q = deque([])
for i in range(1, 10):
    q.append(str(i))
ans = 0
while ans != K:
    l = q.popleft()
    ans += 1
    if ans == K:
        print(l)
        sys.exit()
    if l[-1] == '0':
        q.append(l + '0')
        q.append(l + '1')
    elif l[-1] == '9':
        q.append(l + '8')
        q.append(l + '9')
    else:
        q.append(l + str(int(l[-1]) - 1))
        q.append(l + str(int(l[-1])))
        q.append(l + str(int(l[-1]) + 1))