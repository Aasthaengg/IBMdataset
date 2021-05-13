from collections import deque
N, M = map(int, input().split())
P = list(map(int, input().split()))
K = [[] for _ in range(N)]
for i in range(M):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    K[x].append(y)
    K[y].append(x)
used = [0]*N
OK = []
for i in range(N):
    P[i] -= 1
    if i == P[i]:
        OK.append(i)
ans = 0
for i in range(N):
    if used[i] == 0:
        used[i] = 1
        S = deque([i])
        Enable = [i]
        Origin = [P[i]]
        while S:
            t = S.popleft()
            for j in K[t]:
                if used[j] == 0:
                    used[j] = 1
                    Enable.append(j)
                    Origin.append(P[j])
                    S.append(j)
        T_1 = list(set(OK + Enable))
        T_2 = list(set(OK + Origin))
        ans = max(ans, len(T_1) + len(T_2) - len(set(T_1 + T_2)))

print(ans)