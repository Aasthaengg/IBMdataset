n, q = map(int, input().split())
l = [list(input().split()) for i in range(n)]
from collections import deque
que = deque([[l[i][0], int(l[i][1])] for i in range(n)])
a = []
time = 0
while que != deque([]):
    a = que.popleft()
    if a[1] <= q:
        time += a[1]
        print("{} {}".format(a[0], str(time)))
    else:
        time += q
        a[0], a[1] = a[0], a[1] - q
        que.append(a)