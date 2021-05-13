from collections import defaultdict
import heapq

H, W, M = map(int, input().split())

col_cnt = [0] * W
row_cnt = [0] * H
col_max = 0
row_max = 0

w2h = defaultdict(list)
h2w = defaultdict(list)
bombs = set()

for _ in range(M):
    h, w = map(lambda x:int(x)-1, input().split())
    row_cnt[h] += 1
    col_cnt[w] += 1
    row_max = max(row_max, row_cnt[h])
    col_max = max(col_max, col_cnt[w])
    bombs.add((h, w))

max_rows = set()
max_cols = set()

for h in range(H):
    if row_cnt[h] == row_max:
        max_rows.add(h)
for w in range(W):
    if col_cnt[w] == col_max:
        max_cols.add(w)

cnt = 0
for h, w in bombs:
    if h in max_rows and w in max_cols:
        cnt += 1

if cnt == len(max_rows) * len(max_cols):
    print(row_max + col_max-1)
else:
    print(row_max + col_max)

