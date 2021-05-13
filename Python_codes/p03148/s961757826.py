from heapq import heappush, heappop
from operator import itemgetter
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
e = []
for _ in range(n):
    t, d = map(int, input().split())
    t -= 1
    e.append((d, t))

e.sort(key=itemgetter(0), reverse=True)

b = e[:k]  # 暫定選択（おいしさ基礎ポイント降順取得）

used = [False] * n
hq = []

ans = 0  # 暫定選択（おいしさ基礎ポイント降順取得）
tn = 0  # 種類数
for d, t in b:
    if not used[t]:
        used[t] = True
        tn += 1
    else:
        heappush(hq, (d, t))
    ans += d
ans += pow(tn, 2)  # 種類ボーナス

c = e[k:]  # 取得しなかった予備

# print(b)
# print(c)
# print(hq)
# print(used)
s = ans
cur = 0
while hq:
    d, t = heappop(hq)
    s -= d
    changed = False
    while cur < n - k:
        cd, ct = c[cur]
        cur += 1
        if not used[ct]:
            used[ct] = True
            changed = True
            s += cd
            s += tn * 2 + 1
            tn += 1
            if s > ans:
                ans = s
            break
    if not changed:
        break
print(ans)
