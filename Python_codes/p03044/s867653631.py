from collections import deque

n = int(input())

g = [[] for _ in range(n)]
# 0indexに直している
for i in range(n - 1):
    u, v, w = map(int, input().split())
    g[u - 1].append((v - 1, w))
    g[v - 1].append((u - 1, w))

"""
根から各頂点への距離をd_iとする
2頂点u,vについて、その最小共通祖先をwとすると
uとvの距離=d_u+d_v-2d_w
第3項は常に偶数
d_uとd_vの偶奇が等しければ全体は偶数、偶奇が異なれば全体は奇数
例えば、d_iが偶数なら白に、奇数なら黒に塗るとすれば条件を満たす
"""

dq = deque([0])

# 各頂点について、根からの距離
# 頂点0を根とする
dist_list = [-1] * n
dist_list[0] = 0

# BFS
while dq:
    now = dq.popleft()
    # tと繋がっている各頂点について
    for info in g[now]:
        next = info[0]
        d = info[1]
        if dist_list[next] == -1:
            # 根からtまでの距離 + tから次への距離
            dist_list[next] = dist_list[now] + d
            dq.append(next)

# 偶数なら白、奇数なら黒とする。白黒は逆でも良い。
for i in dist_list:
    if i % 2 == 0:
        print(0)
    else:
        print(1)
