import sys
import numpy as np
input = sys.stdin.buffer.readline

INF = 10 ** 9

N, Ma, Mb = map(int, input().split())
abcs = [tuple(map(int, input().split())) for _ in range(N)]

delta_c = [(Mb * a - Ma * b, c) for a, b, c in abcs]

cost = INF
positives = []
negatives = []
for delta, c in delta_c:
    if delta == 0:
        cost = min(cost, c)
    elif delta > 0:
        positives.append((delta, c))
    else:
        negatives.append((-delta, c))

dp_pos = np.full(401, INF, np.int64)
dp_pos[0] = 0
for delta, c in positives:
    dp_pos[delta:] = np.minimum(dp_pos[:-delta] + c, dp_pos[delta:])

dp_neg = np.full(401, INF, np.int64)
dp_neg[0] = 0
for delta, c in negatives:
    dp_neg[delta:] = np.minimum(dp_neg[:-delta] + c, dp_neg[delta:])

cost = min(cost, np.amin(dp_pos[1:] + dp_neg[1:]))
if cost >= INF:
    print(-1)
else:
    print(cost)
