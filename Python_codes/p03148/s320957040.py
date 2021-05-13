from collections import defaultdict
import heapq
import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)
U = 10 ** 5 + 1

N, K = map(int, input().split())
DT = []
for _ in range(N):
    t, d = map(int, input().split())
    DT.append((d, t))

DT.sort(reverse=True)
score = 0
kind = defaultdict(list)
used = [0] * (U + 1)
for d, t in DT[:K]:
    score += d
    used[t] += 1
    kind[t].append(d)

cnt = len(kind)
ans = score + (cnt * cnt)

cand = []  # 交換する可能性のあるやつ, 小さいやつから削除
for key, val in kind.items():
    val.sort(reverse=True)
    while len(val) > 1:
        heapq.heappush(cand, (val.pop(), key))


for d_in, t_in in DT[K:]:
    if not cand:
        break
    if used[t_in]:
        continue

    d_out, t_out = heapq.heappop(cand)
    used[t_in] += 1
    used[t_out] -= 1
    cnt += 1
    score = score - d_out + d_in
    ans = max(ans, score + (cnt * cnt))

print(ans)