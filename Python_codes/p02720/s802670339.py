from collections import deque

K = int(input())

q = deque()

for i in range(1, 10):
    q.appendleft(i)

cnt = 0

while True:
    a = q.pop()
    cnt += 1
    if cnt == K:
        print(a)
        exit()
    for i in (-1, 0, 1):
        m = a % 10 + i
        if not m < 0 and not m > 9:
            q.appendleft(a * 10 + m)