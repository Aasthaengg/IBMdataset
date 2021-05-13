import collections
N,M = map(int,input().split())
edge = collections.defaultdict(list)
for _ in range(M):
    u,v = map(int,input().split())
    edge[u-1].append(v-1)
S,T = map(int,input().split())
dp = [[-3 for _ in range(3)] for _ in range(N)]
dp[S-1][0] = 0
q = collections.deque()
q.append((S-1,0))
while q:
    p,step = q.popleft()
    next_step = (step+1)%3
    for e in edge[p]:
        if dp[e][next_step] == -3:
            dp[e][next_step] = dp[p][step] + 1
            q.append((e,next_step))
            if e == T-1 and next_step == 0:
                break
print(dp[T-1][0] // 3)