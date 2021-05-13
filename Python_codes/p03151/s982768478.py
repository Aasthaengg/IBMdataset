from collections import deque
n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = [ai - bi for ai, bi in zip(a, b)]
if sum(c) < 0:
    print(-1)
    exit()
c.sort()
minus = deque()
for ci in c:
    if ci >= 0:
        break
    minus.append(ci)
ans = len(minus)
s = sum(minus) * (-1)
plus = 0
idx = -1
while s > plus:
    plus += c[idx]
    ans += 1
    idx -= 1
print(ans)