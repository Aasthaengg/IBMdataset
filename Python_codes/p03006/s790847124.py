
from collections import defaultdict

N = int(input())
X = [list(map(int, input().split())) for _ in range(N)]

X.sort()
ctr = defaultdict(int)
for i in range(N - 1):
    for j in range(i + 1, N):
        p = X[i][0] - X[j][0]
        q = X[i][1] - X[j][1]
        ctr[(p, q)] += 1
        ctr[(-p, -q)] += 1

if N == 1:
    print(1)
else:
    print(N - max(ctr.values()))
