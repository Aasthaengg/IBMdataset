from collections import defaultdict
N,K,L = map(int,input().split())

root_road = list(range(N))
root_rail = list(range(N))
depth_road = [1 for _ in range(N)]
depth_rail = [1 for _ in range(N)]

def find(a,root):
    if root[a] == a:
        return a
    else:
        root[a] = find(root[a],root)
        return root[a]

def unite(a,b,root,depth):
    A = find(a,root)
    B = find(b,root)
    if A == B:
        return
    elif depth[A] > depth[B]:
        root[B] = A
        depth[A] += depth[B]
    else:
        root[A] = B
        depth[B] += depth[A]

for i in range(K):
    p,q = map(int,input().split())
    unite(p-1,q-1,root_road,depth_road)
for i in range(L):
    r,s = map(int,input().split())
    unite(r-1,s-1,root_rail,depth_rail)
d = defaultdict(int)
pairs = []
for i in range(N):
    road = find(i,root_road)
    rail = find(i,root_rail)
    pairs.append((road,rail))
    d[(road,rail)] += 1
for p in pairs:
    print(d[p],end = " ")