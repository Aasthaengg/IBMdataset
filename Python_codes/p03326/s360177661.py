n, m = map(int, input().split())
cakes = [list(map(int, input().split())) for _ in range(n)]

import itertools

ans = 0
for a, b, c in itertools.product([-1, 1], repeat=3):
    li = []
    for i in range(n):
        x = a*cakes[i][0] + b*cakes[i][1] + c*cakes[i][2]
        li.append(x)
    li.sort(reverse=True)
    ans = max(ans, sum(li[:m]))
print(ans)