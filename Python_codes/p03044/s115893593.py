import sys
INF = 10**18
import sys
from heapq import heapify,heappop,heappush,heappushpop


class PriorityQueue:
    
    #初期化
    def __init__(self,heap):
        self.heap = heap
        heapify(self.heap)
    
    #値の追加
    def push(self,item):
        heappush(self.heap,item)
    
    #値の取り出し
    def pop(self):
        return heappop(self.heap)
    
    #値を追加して取り出し
    def pushpop(self,item):
        return heappushpop(self.heap,item)
    
    #データ構造の中身を見る
    def __call__(self):
        return self.heap
    
    #heapの長さ
    def __len__(self):
        return len(self.heap)

def dijkstra(s):
    #始点sから各頂点への最短距離
    d = [INF] * n
    used = [True] * n #True:未確定
    d[s] = 0
    used[s] = False
    edgelist = []
    q = PriorityQueue(edgelist)
    for e in edge[s]:
        q.push(e)
    while len(edgelist):
        minedge = q.pop()
        #まだ使われてない頂点の中から最小の距離のものを探す
        if not used[minedge[1]]:
            continue
        v = minedge[1]
        d[v] = minedge[0]
        used[v] = False
        for e in edge[v]:
            if used[e[1]]:
                q.push([e[0]+d[v],e[1]])
    return d

if __name__ == "__main__":
    n = int(input())
    edge = [[] for i in range(n)]
    for i in range(n-1):
        u,v,w = map(int,input().split())
        u-=1
        v-=1
        edge[u].append([w,v])
        edge[v].append([w,u])
    ans = dijkstra(0)
    c_ans = [0]*n
    for i in range(n):
        if ans[i]%2 == 0:
            c_ans[i] = 0
        else:
            c_ans[i] = 1
    for i in range(n):
        print(c_ans[i])