from collections import deque
a = deque(list(input()))
b = deque(list(input()))
c = deque(list(input()))
now = "a"
win = None
while 1:
    if now == "a":
        if not a:
            win = "A"
            break
        now = a.popleft()
    elif now == "b":
        if not b:
            win = "B"
            break
        now = b.popleft()
    else:
        if not c:
            win = "C"
            break
        now = c.popleft()
print(win)