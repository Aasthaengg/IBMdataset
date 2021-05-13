from collections import deque
N = int(input())
T = [[] for _ in range(N)]
for i in range(N-1):
    u, v, w = map(int, input().split())
    u, v, w = u-1, v-1, w % 2
    T[u].append([v, w])
    T[v].append([u, w])

Ans = [-1]*N
P = deque([0])
Ans[0] = 0
while(len(P) > 0):
    a = P.popleft()
    for i in T[a]:
        if Ans[i[0]] == -1:
            if i[1] == 0:
                Ans[i[0]] = Ans[a]
            else:
                Ans[i[0]] = (Ans[a] + 1) % 2
            P.append(i[0])
for i in Ans:
    print(i)