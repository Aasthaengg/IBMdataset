def examA():
    N, A, B = LI()
    ans = min(A*N,B)
    print(ans)
    return

def examB():
    N, D = LI()
    X = [LI() for _ in range(N)]
    ans = 0
    for i,j in itertools.combinations(X,2):
        cur = 0
        for k in range(D):
            cur += (i[k]-j[k])**2
        cur **=0.5
        if cur==int(cur):
            ans +=1
    print(ans)
    return

def examC():
    L, R = LI()
    cur = []; ans = 10**9
    for i in range(L,min(2019+L,R)+1):
        if i%2019==0:
            ans = 0
            break
        else:
            cur.append(i%2019)
    if ans==0:
        print(ans)
        return
    N = len(cur)
    for i,j in itertools.combinations(cur,2):
        ans = min(ans,(i*j)%2019)
    print(ans)
    return

def examD():
    N = I()
    A = LI()
    dis = [0]*N
    for i in range(N):
        cur = A[i-N+1]-A[i-N]
        dis[i] = cur*2
#    print(dis)
    ans = [0]*N
    for i in range(2,2*N,2):
        ans[i-N] = ans[i-N-2] + dis[i-N-2]
#    print(ans)
    ad = (sum(A) - sum(ans))//N
    for i in range(N):
        ans[i] += ad
    print(" ".join(map(str,ans)))
    return

def bfs(n,e,fordfs,K):
    #点の数、スタートの点、有向グラフ
    W = K
    que = deque()
    que.append(e)
    len = [10**9]*n
    len[e] = 0
    while que:
        now = que.popleft()
        nowlen = len[now]
        cur = K-min(2,nowlen+1)
        for ne in fordfs[now]:
            if len[ne] == 10**9:
                W *=cur; W %=mod
                cur -=1
                len[ne] = nowlen+1
                que.append(ne)
    return W
def examE():
    N, K = LI()
    V = [[]for _ in range(N)]
    for _ in range(N-1):
        a,b = LI()
        V[a-1].append(b-1)
        V[b-1].append(a-1)
    ans = bfs(N,0,V,K)
    print(ans)
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,inf
mod = 10**9 + 7
inf = float('inf')

if __name__ == '__main__':
    examE()
