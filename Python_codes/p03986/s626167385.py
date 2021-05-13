x = input()
from collections import deque

q = deque()
ans = ""
for i in x:
    if i == "S":
        q.append(i)
    else:
        if q:
            q.popleft()
        else:
            ans += "T"
while q:
    ans += q.popleft()
print(len(ans))
