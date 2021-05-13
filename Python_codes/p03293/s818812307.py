from collections import deque
s = deque(list(input()))
t = deque(list(input()))


cnt = 0
while cnt < 100000:
    last = s.pop()
    s.appendleft(last)
    if s == t:
        print('Yes')
        exit()
    cnt += 1
print('No')