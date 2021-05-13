N, M = map(int, input().split())
ab = [map(int, input().split()) for _ in range(M)]
a, b = [list(i) for i in zip(*ab)]

path = [0]*N

for i in range(M):
    path[a[i]-1] += 1
    path[b[i]-1] += 1

for v in path:
    print(v)