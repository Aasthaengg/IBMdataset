N = int(input())

from collections import deque,defaultdict
G = defaultdict(deque)
for i in range(1,N+1):
    t = [int(i) for i in input().split(' ')]
    for j in range(t[1]):
        G[t[0]].append(t[j+2])

time = 1
arrive_time = [-1] * (N + 1) # 到着時刻
finish_time = [-1] * (N + 1) # 到着時刻

def dfs(G,s):
    global time
    stack = deque([s])
    arrive_time[s] = time
    while stack:
        t = stack[-1]
        if G[t]:
            w = G[t].popleft()
            if arrive_time[w] >= 0:
                continue
            elif w in stack:
                continue
            else:
                time += 1
                arrive_time[w] = time
                stack.append(w)
        else:
            time += 1
            finish_time[t] = time
            stack.pop()
            
    return arrive_time,finish_time

for i in range(1,N+1):
    if arrive_time[i] < 0:
        arrive,finish = dfs(G,i)
        time += 1

for i, (a, f) in enumerate(zip(arrive,finish)):
    if not i == 0:
        print(i,a,f)
