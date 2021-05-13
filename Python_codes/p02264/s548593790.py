n, q = [int(i) for i in input().split()]

name = []
time = []

for i in range(n):
    x, y = [i for i in input().split()]
    y = int(y)
    name.append(x)
    time.append(y)

from collections import deque
time = deque(time)
name = deque(name)

count = 0
time_out = []
name_out = []

while len(time) > 0:
    a = time.popleft()
    b = name.popleft()
    if a > q:
        a -= q
        time.append(a)
        name.append(b)
        count += q
    else:
        count += a
        time_out.append(count)
        name_out.append(b)

for i, j in zip(name_out, time_out):
    print(i, j)

