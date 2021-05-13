import sys
N, M = map(int, input().split())
H = tuple(map(int, input().split()))
G = [set() for _ in range(N)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    G[a-1].add(b-1)
    G[b-1].add(a-1)

ans = 0
for i in range(N):
    h = H[i]
    for j in G[i]:
        if h <= H[j]:
            break
    else:
        ans += 1
print(ans)