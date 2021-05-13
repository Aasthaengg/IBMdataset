from collections import deque

S = input()
X, Y = map(int, input().split())
F = [deque() for _ in (0, 1)]

i = 0
tmp = 0
for s in S:
    if s == 'F':
        tmp += 1
    else:
        F[i].append(tmp)
        i = (i + 1) % 2
        tmp = 0
if tmp:
    F[i].append(tmp)

first = F[0].popleft()

T = [{first}, {0}]
for i in range(2):
    for j in F[i]:
        T[i] = {k - j for k in T[i]} | {k + j for k in T[i]}
if X in T[0] and Y in T[1]:
    print('Yes')
else:
    print('No')
