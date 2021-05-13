import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N = ir()
edges = [set() for _ in range(N+1)] # 1-indexed
for _ in range(N-1):
    a, b = lr()
    edges[a].add(b)
    edges[b].add(a)
    
C = lr()
C.sort(reverse=True)
degrees = [len(x) for x in edges]
deg_1 = [i for i, d in enumerate(degrees) if d == 1]
score = sum(C[1:])
answer = [None] * (N+1)

# start from every leaf
while deg_1:
    leaf = deg_1.pop()
    answer[leaf] = C.pop()
    if not deg_1:
        break
    cand = edges[leaf].pop()
    edges[cand].remove(leaf)
    degrees[cand] -= 1
    if degrees[cand] == 1:
        deg_1.append(cand)

print(score)
print(*answer[1:])
