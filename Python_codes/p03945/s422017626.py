from collections import deque

s = deque(input())
cnt = 0
p = s.pop()
for _ in range(len(s)):
    n = s.pop()
    if n != p:
        cnt += 1
    p = n
print(cnt)