import sys
from itertools import accumulate, product
from operator import itemgetter
read = sys.stdin.read

N, W, *wv = map(int, read().split())
w1 = wv[0]
V = [[0] for _ in range(4)]

for w, v in sorted(zip(*[iter(wv)] * 2), key=itemgetter(1), reverse=True):
    V[w - w1].append(v)


V = list(map(list, map(accumulate, V)))
n = [len(V[i]) for i in range(4)]
answer = 0
for a, b, c in product(range(n[0]), range(n[1]), range(n[2])):
    tmp = b + c * 2 + (a + b + c) * w1
    if tmp > W:
        continue

    d = min(n[3] - 1, (W - tmp) // (w1 + 3))
    v = V[0][a] + V[1][b] + V[2][c] + V[3][d]
    if v > answer:
        answer = v

print(answer)