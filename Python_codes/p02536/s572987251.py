import sys
sys.setrecursionlimit(100000)

N, M = map(int, input().split())

A = []
B = []

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    A.append(a)
    B.append(b)

root = [i for i in range(N)]

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

def unite(x, y):
    x = find(x)
    y = find(y)
    root[y] = x

for i in range(M):
    unite(A[i], B[i])

for x in range(N):
    find(x)

roots = set(root)

print(len(roots) - 1)