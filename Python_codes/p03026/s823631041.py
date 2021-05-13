def examD():
    N = I()
    V = [[]for _ in range(N)]
    for _ in range(N-1):
        A, B = LI()
        V[A-1].append(B-1)
        V[B-1].append(A-1)
    C = LI(); C.sort()
    e = 0
    low = 0; up = N-1
    ans = 0; W = [-1] * N
    # 各点の値
    W[e] = C[up]; up -=1
    que = deque()
    que.append(e)
    while que or low<up:
        now = que.popleft()
        if len(V[now])==1 and now!=0:
            W[now] = C[low]
            ans += W[now]
            low +=1
        elif now!=0:
            W[now] = C[up]
            up -= 1
            ans += W[now]
        for ne in V[now]:
            if W[ne] == -1:
                que.append(ne)
    print(ans)
    print(" ".join(map(str,W)))

from string import digits
import sys,copy,bisect,itertools,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examD()
