N, M = map(int, input().split())
H = list(map(int, input().split()))
g = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

cnt = 0
for n in range(1,N+1):
    for i in g[n]:
        if H[n-1] <= H[i-1]:
            break
    else:
        cnt += 1

print(cnt)
