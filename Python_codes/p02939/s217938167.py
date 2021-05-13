from collections import deque

s = deque(input())
bef = s.popleft()
ans = 1
while (s):
    now = s.popleft()
    if now == bef:
        if s:
            s.popleft()
        else:
            break
        bef = ""
    else:
        bef = now
    ans += 1

print(ans)
