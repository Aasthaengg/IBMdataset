import heapq as hq
from collections import defaultdict
N, Q = map(int, input().split())
event = []
for i in range(N):
    si, ti, xi = map(int, input().split())
    event.append([si - xi, ti - xi, xi])
#STX = [list(map(int, input().split())) for i in range(N)]
Dlist = [int(input()) for i in range(Q)]
#for s,t,x in STX:
#    event.append([s - x, t-x, x])
event.sort(key=lambda x:x[0])
h = []
tdic = defaultdict(int)
ind = 0
for Di in Dlist:
    while ind<N and event[ind][0] <= Di:
        #Diまでに始まった工事を追加
        hq.heappush(h, event[ind][2])
        tdic[event[ind][2]] = event[ind][1]
        ind += 1
    while h and Di >= tdic[h[0]]:
        #Diまでに終わった工事を削除
        hq.heappop(h)
    if h:
        print(h[0])
    else:
        print(-1)