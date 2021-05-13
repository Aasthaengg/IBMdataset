k = int(input())

from collections import deque
d = deque()
for i in range(1,10):
    d.append(i)

count = 0
while True:
    count += 1
    if count == k:
        print(d.popleft())
        exit()
    t = d.popleft()
    r = t % 10
    if r != 0:
        d.append(10*t + r - 1)
    d.append(10*t + r)
    if r != 9:
        d.append(10*t + r + 1)