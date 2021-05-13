from collections import deque
n = int(input())
li = []
l = []
di = {}
for i in range(n):
    a, b = map(int, input().split())
    li.append((a+b, -a, i))
    l.append((b+a, -b, i))
    di[i] = False
li.sort(reverse=True)
l.sort(reverse=True)
li = deque(li)
l = deque(l)
left, right = 0, 0
while li:
    while True and li:
        p = li.popleft()
        if di[p[2]]:
            continue
        di[p[2]] = True
        left += -p[1]
        break
    if len(l) != 0:
        while True and l:
            q = l.popleft()
            if di[q[2]]:
                continue
            di[q[2]] = True
            right += -q[1]
            break
print(left-right)
