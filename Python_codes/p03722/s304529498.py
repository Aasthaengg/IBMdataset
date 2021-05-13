def cin():  return list(map(int,input().split()))

def bellman_ford(s):
    d = [float('inf')] * N
    d[s] = 0
    for i in range(N):
        update = False
        for x, y, z in G:
            if d[y] > d[x] + z:
                d[y] = d[x] + z
                if i == N - 1 and y == N - 1:  return "inf"
    return -d[N - 1]

N, M = cin()
G = []
bfr = []
for i in range(M):
    s, t, w = cin()
    G.append((s - 1, t - 1, -w))
ans = bellman_ford(0)
print(ans)