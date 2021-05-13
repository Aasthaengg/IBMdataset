import sys

stdin = sys.stdin
sys.setrecursionlimit(10 ** 7)

ri = lambda: int(rs())
rl = lambda: list(map(int, stdin.readline().split()))  # applies to only numbers
rs = lambda: stdin.readline().rstrip()  # ignores trailing space

N, K = rl()
max = (N-1) * (N-2) // 2
if K > max:
    print(-1)
    exit()
edges = []
for i in range(2, N+1):
    edges.append((1, i))
count = max - K
for i in range(2, N):
    if count == 0:
        break
    for j in range(i+1, N+1):
        if count == 0:
            break
        edges.append((i, j))
        count -= 1
print(len(edges))
for x in edges:
    print(*x)

