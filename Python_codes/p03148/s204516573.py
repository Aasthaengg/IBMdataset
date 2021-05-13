# 同じ種類だと、点数が高いやつを選ぶ
# 違う種類を選ぶと、ボーナス点が入るので、それをどうするか
# d  = sum(di) + x**x
# 種類xを固定すると？ O(log(N))でいける？
# ※※ 種類が増えるかどうかを降順で見ながらboolで置き換えるという発想。強い。

from collections import defaultdict

di = defaultdict(list)
n, k = map(int, input().split())

sushi = []
kinds = []
for i in range(n):
    t,d = map(int, input().split())
    sushi.append((d,t))
    kinds.append(t)
sushi.sort(reverse=True)
sushidict = defaultdict(int)
n_kind_all = len(set(kinds))

cnt = 0
import heapq
sushiq = []
# まずは上からK個貪欲に取る
for i in range(k):
    d,t = sushi[i]
    heapq.heappush(sushiq,(d,t)) 
    sushidict[t] += 1
    cnt += d

n_kind = len(sushidict)
res = []
res.append(cnt+n_kind**2)

for i in range(k,n):
    d,t = sushi[i]
    # すでにある種類の場合は大丈夫
    if sushidict[t] > 0 : continue
    # 種類が増える時、小さいものから入れ替えていく
    d_min,t_min = heapq.heappop(sushiq)
    # popして消えるようなものはNG
    while sushidict[t_min] == 1 and sushiq:
        d_min, t_min = heapq.heappop(sushiq)
    # popするものがなくなったら終了
    if not sushiq:
        break
    sushidict[t_min] -= 1
    sushidict[t] += 1
    n_kind += 1
    cnt  = cnt - d_min + d
    res.append(cnt+n_kind**2)
    if n_kind == n_kind_all:
        break

print(max(res))
# print(res)