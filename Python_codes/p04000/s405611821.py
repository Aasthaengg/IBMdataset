from collections import defaultdict
from bisect import *
h, w, n = map(int, input().split())

d = defaultdict(list)
q = [list(map(int, input().split())) for i in range(n)]
q.sort()
ans = [0]*10
for i in range(n):
    a, b = q[i]
    d[a].append(b)

for a, b in q:
    for i in range(max(1, a-2), min(h-2, a)+1):
        for j in range(max(1, b-2), min(w-2, b)+1):
            count = 0
            for k in range(3):
                count += bisect_right(d[i+k], j+2) - bisect_left(d[i+k], j)
            ans[count] += 1


for i in range(1, 10):
    ans[i] //= i

ans[0] = (w-2)*(h-2) - sum(ans[1:])
for i in range(10):
    print(ans[i])
