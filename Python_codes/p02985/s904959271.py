from collections import deque

def permutation(n, r):
    if (r < 0) or (n < r):
        return 0

    res = factinv[r] % p
    for i in range(r):
        res = res * (n - i) % p

    return fact[n] * factinv[n-r] % p

def BFS(tree, root):
    N = len(tree)
    dist = [-1]*N

    res = K

    q = deque([root])
    dist[root] = 0

    while q:
        v = q.popleft()
        for n_v in tree[v]:
            if dist[n_v] != -1:
                continue
            dist[n_v] = dist[v] + 1
            q.append(n_v)
        
        child_cnt = len(tree[v])
        if dist[v] > 0:
            child_cnt -= 1

        if child_cnt > 0:
            color = K - 1
            if dist[v] > 0:
                color -= 1
            
            if color < child_cnt:
                res = 0
                break
            else:
                res *= permutation(color, child_cnt)
                res %= p
    
    return res

N, K = map(int, input().split())
tree = [[] for _ in range(N)]

p = 10 ** 9 + 7

fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
 
for i in range(2, K + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

for i in range(N - 1):
    a, b = map(int, input().split())
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)

print(BFS(tree, 0))