import heapq
# python template for atcoder1
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


N = int(input())
adj = [[] for _ in range(N)]

for _ in range(N-1):
    a, b = map(lambda x: int(x)-1, input().split())
    adj[a].append(b)
    adj[b].append(a)

# heapqで大きい順に取り出したいから、マイナスにしておく。
L = list(map(lambda x: -int(x), input().split()))
heapq.heapify(L)
# Maxは一番大きい数字以外の和.(全体の和-最大の整数)でも止める。
# Lはマイナスがかけてあるので、min(L)で最大の和が求まる
score = -sum(L)+min(L)


# nodeに書く数字
node = [-1]*N

# leafを探す,leafからbfsして訪問順に大きい数字を入れていく
leaf = -1
for i, a in enumerate(adj):
    if len(a) == 1:
        leaf = i
        break

# bfs
Q = [leaf]
while Q:
    cur = Q.pop()
    for a in adj[cur]:
        if node[a] == -1:  # まだたどり着いてないとこには、数字を入れる。
            node[a] = - heapq.heappop(L)
            Q.append(a)
print(score)
print("\n".join(map(str, node)))