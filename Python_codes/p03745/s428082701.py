from collections import deque

N = int(input())
A_deque = deque(int(e) for e in input().split())

section = list()
section.append(A_deque.popleft())
ans = 1
mode = 0

while 1:
    if len(A_deque) == 0:
        break
    elif mode == 0:
        next = A_deque.popleft()
        if section[-1] == next:
            section.append(next)
        elif section[-1] > next:
            section.append(next)
            mode = -1
        elif section[-1] < next:
            section.append(next)
            mode = 1
    elif mode == 1:
        next = A_deque.popleft()
        if section[-1] > next:
            section.clear()
            section.append(next)
            ans += 1
            mode = 0
        else:
            section.append(next)
    elif mode == -1:
        next = A_deque.popleft()
        if section[-1] < next:
            section.clear()
            section.append(next)
            ans += 1
            mode = 0
        else:
            section.append(next)

print(ans)