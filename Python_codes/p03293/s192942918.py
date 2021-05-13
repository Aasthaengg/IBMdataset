from collections import deque

s = deque(list(input()))
t = deque(list(input()))
ans = "No"

for i in range(len(s)):
    if s == t:
        ans = "Yes"
        break
    t.rotate()

print(ans)