from collections import deque
ov = deque([0])
n = int(input())
e = [[int(_)-1 for _ in input().split()] for __ in range(n-1)]
c = sorted([int(_) for _ in input().split()])
m = sum(c[:-1])
d = [0 for _ in range(n)]
adv = [[] for _ in range(n)]
for i in range(n-1):
    adv[e[i][0]].append(e[i][1])
    adv[e[i][1]].append(e[i][0])
while len(ov) > 0:
    i = ov.popleft()
    d[i] = c.pop()
    for j in range(len(adv[i])):
        if d[adv[i][j]] == 0:
            ov.append(adv[i][j])
print(m); print(' '.join([str(_) for _ in d]))