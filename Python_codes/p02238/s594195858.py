N = int(input())
UKV = [list(map(int,input().split())) for _ in range(N)]

seen = [False]*N
first_time = [-1]*N
last_time = [-1]*N
time = 0
def dfs(G, v):
    global seen
    global first_time
    global last_time
    global time
    seen[v-1] = True
    time += 1
    first_time[v-1] = time
    for next_v in G[v]:
        if seen[next_v-1]:
            continue
        dfs(G, next_v)
    time += 1
    last_time[v-1] = time

G = {}
for ukv in UKV:
    G[ukv[0]] = sorted(ukv[2:])
for i in range(1,N+1):
    if seen[i-1]:
        continue
    dfs(G, i)

for i in range(1,N+1):
    print(i,first_time[i-1],last_time[i-1])
