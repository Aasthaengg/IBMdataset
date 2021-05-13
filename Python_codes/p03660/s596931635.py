# https://atcoder.jp/contests/abc067/tasks/arc078_b
# 1とNの最短経路について注目したときに、それぞれの最適戦略を考えてみる
# 相手を負かせたい→相手側に攻めて道を塞ぐのが有利(相手のマスが少なくなるから)
# 自分が負けそう→退避して行きたい(でも相手のマスのほうが多かったらもう逆転は不可能)
# 勝者は→先にたどり着けるノードの中で多い方が勝者(同数の場合はFennecが敗者)

import sys
read = sys.stdin.readline
from collections import defaultdict, deque


def read_ints():
    return list(map(int, read().split()))


N = int(input())
graph = defaultdict(lambda: [])
for _ in range(N - 1):
    a, b = read_ints()
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)


def ret_dists(u):
    ret = [-1] * N
    que = deque([(u, -1, 0)])  # 現在のノード、前のノード、距離
    ret[u] = 0
    while que:
        u, p, d = que.popleft()
        nd = 1 + d
        for nu in graph[u]:
            if nu == p:  # 親はもう探索しない
                continue
            ret[nu] = nd
            que.append((nu, u, nd))

    return ret


fennec_dist = ret_dists(0)
snuke_dist = ret_dists(N - 1)

n_snuke = 0  # snukeに近いノードの数
n_fennec = 0  # 0を含んでfennecに近い #fennecが濡れるので
for f, s in zip(fennec_dist, snuke_dist):
    if f > s:  # すぬけにちかい
        n_snuke += 1
    else:
        n_fennec += 1

# print(n_fennec, n_snuke)
if n_fennec > n_snuke:
    print('Fennec')
else:
    print('Snuke')
