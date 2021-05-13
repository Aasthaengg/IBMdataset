from collections import deque
mod = 10**9+7
N,K = map(int,input().split())
Tree = [[] for _ in range(N+1)]
for i in range(N-1):
    ai,bi = map(int,input().split())
    Tree[ai].append(bi)
    Tree[bi].append(ai)
d = deque([1])
parent = [-1]*(N+1)
permutation = [1,K-2]
for i in range(K-3):
    permutation.append(permutation[-1]*(K-3-i)%mod)
while d:
    x = d.popleft()
    for y in Tree[x]:
        if parent[x] != y:
            parent[y] = x
            d.append(y)
    if x == 1:
        if len(Tree[x]) > K-1:
            ans = 0
        else:
            ans = 1
            for i in range(len(Tree[x])+1):
                ans *= K-i
                ans %= mod
    else:
        if len(Tree[x]) > K-1:
            ans = 0
        else:
            ans *= permutation[len(Tree[x])-1]
            ans %= mod
print(ans)