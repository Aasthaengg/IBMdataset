from collections import deque
S = input()
T = input()

s = deque(list(S))
t = deque(list(T))

n = len(s)
for i in range(n):
    if t == s:
        print("Yes")
        break
    a = t.popleft()
    t.append(a)
else:
    print("No")
