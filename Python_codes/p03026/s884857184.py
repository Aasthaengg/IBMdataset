def examA():
    N = I()
    ans = 0
    print(ans)
    return

def examB():
    ans = 0
    print(ans)
    return

def examC():
    ans = 0
    print(ans)
    return

def examD():
    def bfs(n, e, fordfs, C):
        # 点の数、スタートの点、有向グラフ
        W = [-1] * n
        # 各点の状態量、最短距離とか,見たかどうかとか
        i = 0
        W[e] = C[i]
        i += 1
        que = deque()
        que.append(e)
        while que and i<n:
            now = que.popleft()
            for ne in fordfs[now]:
                if W[ne] == -1:
                    W[ne] = C[i]
                    i += 1
                    que.append(ne)
        return W
    N = I()
    V = [[]for _ in range(N)]
    for _ in range(N-1):
        A, B = LI()
        V[A-1].append(B-1)
        V[B-1].append(A-1)
    C = LI(); C.sort(reverse=True)
    e = 0
    ans = bfs(N,e,V,C)
    print(sum(ans)-C[0])
    print(" ".join(map(str,ans)))
    return

def examE():
    ans = 0
    print(ans)
    return

def examF():
    ans = 0
    print(ans)
    return

import sys,copy,bisect,itertools,heapq,math,random
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = 10**(-12)
alphabet = [chr(ord('a') + i) for i in range(26)]

if __name__ == '__main__':
    examD()

"""

"""