import sys
LI = lambda : [int(x) for x in sys.stdin.readline().split()]

N,M = LI()
island = [0 for _ in range(N)]
req = [[] for _ in range(N)]
for _ in range(M):
    a,b = LI()
    req[a-1].append(b-1)

p = 1
ans = 0
for i in range(N):
    if island[i] > p:
        ans += 1
        p = island[i]
    for b in req[i]:
        island[b] = p+1
print(ans)