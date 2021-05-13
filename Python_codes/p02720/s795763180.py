from collections import deque

k = int(input())


if k < 10:
    print(k)
    exit()

q = deque()
lun = []
for i in range(1, 10):
    q.append(i)
    lun.append(i)

cnt = 9
while cnt < k:
    x = q.popleft()
    if x % 10 == 0:
        nx = 10 * x
        q.append(nx)
        lun.append(nx)
        nx = 10 * x + 1
        q.append(nx)
        lun.append(nx)
        cnt += 2
    elif x % 10 == 9:
        nx = 10 * x + 8
        q.append(nx)
        lun.append(nx)
        nx = 10 * x + 9
        q.append(nx)
        lun.append(nx)
        cnt += 2
    else:
        m = x % 10
        nx = 10 * x + m - 1
        q.append(nx)
        lun.append(nx)
        nx = 10 * x + m
        q.append(nx)
        lun.append(nx)
        nx = 10 * x + m + 1
        q.append(nx)
        lun.append(nx)
        cnt += 3
lun.sort()
print(lun[k-1])
