import heapq
import sys
input=sys.stdin.readline

N,Q = map(int,input().split(" "))
querys = []
START = 1
GOAL = 0
GO = 2

for _ in range(N):
    s,t,x = (map(int,input().split(" ")))
    s -=(x + 0.5)
    t -= (x + 0.5)
    querys.append( (s,START,x) )
    querys.append( (t,GOAL,x) )

for _ in range(Q):

    querys.append( (int(input()),GO,-1)  )
koji_place = []
koji_um = set([])
heapq.heapify(koji_place)
querys.sort()
for query in querys:
    time,qtype,place = query
    if qtype == START:
        heapq.heappush(koji_place,place)
        koji_um.add(place)
    elif qtype == GOAL:
        koji_um.remove(place)
    else:
        while koji_place and koji_place[0] not in koji_um: #更新と最近の場所のチェックを同時に行う
            heapq.heappop(koji_place) #koji place のpopは最大で place分，つまり合計で10 ** 5回行われるため ここのwhile
            # はOに影響を与えない
        if not koji_place:
            print(-1)
        else:
            print(koji_place[0])



