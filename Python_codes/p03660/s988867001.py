from collections import deque

n = int(input())

roots = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = map(int,input().split())
    roots[a-1].append(b-1)
    roots[b-1].append(a-1)

d1 = [-1] * n
d2 = [-1] * n
d1[0] = 0
d2[-1] = 0

q1 = deque([0])
q2 = deque([n-1])

while q1:
    l = q1.pop()
    for i in roots[l]:
        if d1[i] == -1:
            d1[i] = d1[l] + 1
            q1.append(i)

while q2:
    l = q2.pop()
    for i in roots[l]:
        if d2[i] == -1:
            d2[i] = d2[l] + 1
            q2.append(i)

f = 0
s = 0

for i in range(n):
    if d1[i] <= d2[i]:
        f += 1
    else:
        s += 1

if f > s:
    print('Fennec')
else:
    print('Snuke')
