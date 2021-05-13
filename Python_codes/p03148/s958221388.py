import heapq

INF=10**12

N, K = map(int,input().split())
td = [[0,0] for i in range(N)]
s = [[] for i in range(N)]

for i in range(N):
    td[i][0], td[i][1] = map(int,input().split())
    td[i][0] -= 1
    s[td[i][0]].append(td[i][1])

for i in range(N):
    if s[i] == []:
        s[i].append(-INF)
    s[i].sort(key=lambda x:-x)

s.sort(key=lambda x:-x[0])

tmp = 0
q = []

for i in range(K):
    tmp += s[i][0]
    for j in range(1,len(s[i])):
        heapq.heappush(q,-s[i][j])
for i in range(K,N):
    for j in range(len(s[i])):
        heapq.heappush(q,-s[i][j])

res = tmp + K * K

for i in range(1,K)[::-1]:
    v = s[i][0]
    if q == []: break
    w = - q[0]
    if v < w:
        tmp = tmp + w - v
        heapq.heappop(q)
        heapq.heappush(q,-v)
    res = max(res, tmp + i * i)        

print(res)