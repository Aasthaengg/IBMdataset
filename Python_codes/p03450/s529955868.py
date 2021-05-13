N,M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    l,r,d = map(int, input().split())
    E[l-1].append((r-1, d))
    E[r-1].append((l-1, -d))

from collections import deque
human = ["0"]*N
ans = "Yes"
for i in range(N):
    if ans == "No":
        break
    if len(E[i]) == 0:
        continue
    if human[i] == "0":
        human[i] = 0
        q = deque([i])
        while q:
            temp = q.popleft()
            for e in E[temp]:
                if human[e[0]] == "0":
                    human[e[0]] = human[temp]+e[1]
                    q.append(e[0])
                elif human[e[0]] != human[temp]+e[1]:
                    ans = "No"
                    break
    else:
        for e in E[i]:
            if human[e[0]] != human[i]+e[1]:
                ans = "No"
                break

print(ans)