
import heapq

N = int(input())

es = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = map(int, input().split())
    es[a-1].append(b-1)
    es[b-1].append(a-1)

INF = float("inf")


# ダイクストラでフェネック君の開始地点からの距離を探索
dist_f = [INF] * N
dist_f[0] = 0
q = [(0,0)]
while q:
    cost, curr = heapq.heappop(q)
    if dist_f[curr] < cost:
        continue
    for nxt in es[curr]:
        if dist_f[nxt] < dist_f[curr] + 1:
            continue
        dist_f[nxt] = dist_f[curr] + 1
        heapq.heappush(q, (dist_f[nxt], nxt))

# ダイクストラですぬけ君の開始地点からの距離を探索
dist_s = [INF] * N
dist_s[N-1] = 0
q = [(0,N-1)]
while q:
    cost, curr = heapq.heappop(q)
    if dist_s[curr] < cost:
        continue
    for nxt in es[curr]:
        if dist_s[nxt] < dist_s[curr] + 1:
            continue
        dist_s[nxt] = dist_s[curr] + 1
        heapq.heappush(q, (dist_s[nxt], nxt))

cnt_f = 0
cnt_s = 0
for i in range(1,N-1):
    if dist_f[i] <= dist_s[i]:
        cnt_f += 1
    else:
        cnt_s += 1

if cnt_f > cnt_s:
    print("Fennec")
else:
    print("Snuke")

