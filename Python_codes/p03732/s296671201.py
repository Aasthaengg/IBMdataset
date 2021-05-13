from collections import defaultdict
from itertools import accumulate
N, W = map(int, input().split())
w = [0] * N; v = [0] * N
d = defaultdict(list)
for i in range(N):
    w[i], v[i] = map(int, input().split())
    d[w[i]].append(v[i])

for i in range(4):
    d[w[0]+i].sort(reverse=True)
    d[w[0]+i].insert(0, 0)
    d[w[0]+i] = list(accumulate(d[w[0]+i]))


ans = 0
for i in range(len(d[w[0]])):
    for j in range(len(d[w[0]+1])):
        for k in range(len(d[w[0]+2])):
            for l in range(len(d[w[0]+3])):
                if i * w[0] + j * (w[0] + 1) + k * (w[0] + 2) + l * (w[0] + 3) <= W:
                    ans = max(ans, d[w[0]][i] + d[w[0]+1][j] + d[w[0]+2][k] + d[w[0]+3][l])
print(ans)
