# dequeでいくわ
from collections import deque
n = int(input())
a = list(input().split())
ans = deque()
for i in range(n):
    if i % 2 == 0:
        ans.append(a[i])
    else:
        ans.appendleft(a[i])
if n % 2 == 1:
    ans = list(ans)[::-1]
print(" ".join(ans))