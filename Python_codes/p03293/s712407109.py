from collections import deque
s = list(input())
t = list(input())

sd = deque(s)
n = len(s)
for i in range(n):
    if list(sd) == t:
        print('Yes')
        exit()
    sd.appendleft(sd.pop())

print('No')