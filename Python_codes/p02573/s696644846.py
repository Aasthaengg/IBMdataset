n, m = map(int, input().split())
a, b = [], []
for i in range(m):
  _, __ = map(int, input().split())
  _ -= 1
  __ -= 1
  a.append(_)
  b.append(__)
  
# union-find

# 誰の肩に手を置いているか（先頭の場合は-1）
parent = [-1 for i in range(n)]

# 列車の深さ
depth = [0 for i in range(n)]

# kさんの「運転手」が誰かを調べる関数
def find_root(k):
  while parent[k] != -1:
    k = parent[k]
  return k 

for i in range(m):
  # a[i] と b[i] の合併
  root_a = find_root(a[i])
  root_b = find_root(b[i])
  if root_a == root_b: continue
  
  # 浅い列車を持っている方が負けるようにする
  if depth[root_a] > depth[root_b]:
    root_a, root_b = root_b, root_a
  parent[root_a] = root_b
  depth[root_b] = max(depth[root_a]+1, depth[root_b])
  
group = [find_root(i) for i in range(n)]

from collections import Counter
print(Counter(group).most_common()[0][1])