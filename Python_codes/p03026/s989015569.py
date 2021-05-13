import sys
sys.setrecursionlimit(10**7)
def lmi(): return list(map(int, input().split()))

n = int(input())
e = []
tree = [[] for i in range(n)]
w = [-1] * n
for i in range(n-1):
    a, b = lmi()
    a -= 1; b -= 1
    e.append([a, b])
    tree[a].append(b)
    tree[b].append(a)

c = lmi()
c.sort()

def dfs(x):
    if len(c) == 0:
        return
    if w[x] == -1:
        w[x] = c.pop()
        for i in tree[x]:
            dfs(i)

dfs(0)

print(sum([min(w[i],w[j]) for i, j in e]))
print(' '.join(map(str, w)))
