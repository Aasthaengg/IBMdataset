import sys
from collections import defaultdict
from itertools import accumulate

input = sys.stdin.readline

N, K = map(int, input().split())
sushi = defaultdict(list)
for i in range(N):
    t, d = map(int, input().split())
    sushi[t].append(d)

X, Y = [], []
for v in sushi.values():
    v = sorted(v, reverse=True)
    X.append(v[0])
    if len(v) > 1:
        Y += v[1:]
X = sorted(X, reverse=True)
Y = sorted(Y, reverse=True)

X = [0] + [x for x in accumulate(X)]
Y = [0] + [x for x in accumulate(Y)]

ans = 0
for i in range(1, min(len(X), K + 1)):
    j = K - i
    if j < len(Y):
        ans = max(ans, X[i] + Y[j] + i * i)
print(ans)
