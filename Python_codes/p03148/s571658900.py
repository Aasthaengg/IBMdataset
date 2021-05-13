import heapq
from collections import defaultdict
N, K = map(int, input().split())

sushi = defaultdict(list)
for i in range(N):
    t, d = map(int, input().split())
    sushi[t].append(d)

# 各種類で最大のもの
P = []
# Pに入らなかったもの
Q = []

for k in sushi.keys():
    # 最大のものだけ
    sushi[k].sort(reverse=True)
    P.append(sushi[k][0])
    for x in sushi[k][1:]:
        Q.append(-x)

# heapqで最小値を扱う
heapq.heapify(P)
# heapqで最大値を扱う
heapq.heapify(Q)

cur = 0
# 全種類食べることが出来る場合
if K >= len(sushi.keys()):
    max_variation = len(sushi.keys())
    # 全種類について、最大のものを食べる
    cur += sum(P)
    # まだ食べられるので、Qを大きい方から食べる
    for _ in range(K - max_variation):
        cur += -heapq.heappop(Q)
    ans = cur + max_variation**2
# 全種類食べることが出来ない場合
else:
    # 最大値が大きい方からからK種類だけPに残す
    # 選べなかったものはQに突っ込む
    while len(P) > K:
        m = heapq.heappop(P)
        heapq.heappush(Q, -m)
    max_variation = K
    cur += sum(P)
    ans = cur + max_variation**2

# max_variation-1, ..., 1種類食べるとき
for i in range(max_variation - 1, 0, -1):
    # Pのうち、最小のものは一旦諦める
    p = heapq.heappop(P)
    cur -= p

    # 諦めたものをQに入れて、Qから最大のものを1つ食べる
    # 結果的にi種類ではなくなる場合もあるが、無視できる
    heapq.heappush(Q, -p)
    cur += -heapq.heappop(Q)
    ans = max(ans, cur + i**2)

print(ans)
