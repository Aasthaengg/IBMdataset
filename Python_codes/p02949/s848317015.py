import sys
N, M, P = map(int, input().split())

Edgeinv = [[] for _ in range(N+1)]
Edge = [[] for _ in range(N+1)]
inf = 2*10**10
Edgenum = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]
for a, b, c in Edgenum:
    Edgeinv[b].append(a)
    Edge[a].append(b)

used = set([N])
stack = [N]
while stack:
    vn = stack.pop()
    for vf in Edgeinv[vn]:
        if vf not in used:
            used.add(vf)
            stack.append(vf)

used2 = set([1])
stack = [1]
while stack:
    vn = stack.pop()
    for vf in Edge[vn]:
        if vf not in used2:
            used2.add(vf)
            stack.append(vf)

Edgenum = [(a, b, c) for a, b, c in Edgenum if a in used and b in used]

used &= used2

dp = [-inf]*(N+1)
dp[1] = 0
for i in range(N-1):
    dp2 = dp[:]
    for a, b, c in Edgenum:
        dp2[b] = max(dp2[b], dp[a] + c - P)
    dp = dp2[:]

Dp = dp[:]
for i in range(N):
    dp2 = dp[:]
    for a, b, c in Edgenum:
        dp2[b] = max(dp2[b], dp[a] + c - P)
    dp = dp2[:]

if any(Dp[i] < dp2[i] for i in used):
    print(-1)
else:
    print(max(0, Dp[N]))
