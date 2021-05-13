from collections import deque


def perm(n, k, a=1, mod=10**9+7):
  if n < k or k < 0:
    a = 0
  else:
    for i in range(n, n-k, -1):
      a = a*i % mod
  
  return a


MOD = 10**9 + 7
N, K = map(int, input().split())
tree = [[] for i in range(N)]
for i in range(N-1):
  a, b = map(int, input().split())
  tree[a-1].append(b-1)
  tree[b-1].append(a-1)


ans = K
d = deque([[0, -1]])
while d:
  node, parent = d.pop()
  children = tree[node]
  if parent == -1:
    ans = ans*perm(K-1, len(children)) % MOD
  else:
    ans = ans*perm(K-2, len(children)-1) % MOD
  
  for child in children:
    if child == parent:
      continue
    
    d.append([child, node])

print(ans)