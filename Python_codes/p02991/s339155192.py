from collections import deque
N, M = map(int, input().split())
K = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    K[a-1].append(b-1)
S, T = map(int, input().split())
used = [[0]*3 for _ in range(N)]

q = deque([[S-1, 0, 0]])
used[S-1][0] = 1
ans = [[-3]*3 for _ in range(N)]
while(len(q)>0):
    u, v, c = q.popleft()
    v_n = (v + 1) % 3
    for j in K[u]:
        if used[j][v_n] == 0:
            used[j][v_n] = 1
            ans[j][v_n] = c+1
            q.append([j, v_n, c+1])

print(ans[T-1][0]//3)