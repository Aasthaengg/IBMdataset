S = input()
from collections import deque
q = deque()
ans = 0
for s in S:
    if not q:
        q.append(s)
        continue
    pres = q.pop()
    if (s == '0' and pres == '1') or (s=='1' and pres=='0'):
        ans += 2
    else:
        q.append(pres)
        q.append(s)
print(ans)
