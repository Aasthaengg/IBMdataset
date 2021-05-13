import sys,queue,math,copy,itertools,bisect,collections
from heapq import *

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**18
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())

    N = NI()
    root = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b = LI()
        root[a-1].append(b-1)
        root[b-1].append(a-1)

    node = [-1 for _ in range(N)]
    q = []
    q.append((0,0))
    node[0] = 0
    while q:
        u,num = q.pop()
        for v in root[u]:
            if node[v] < 0:
                node[v] = num+1
                if v == N-1:
                    q = []
                    break
                q.append((v,num+1))
    c = node[N-1]
    u = N-1
    pu = 0
    while c > (node[N-1])//2:
        for v in root[u]:
            if node[v] != c-1: continue
            pu = u
            u = v
            c -= 1
            break

    p = u
    node = [-1 for _ in range(N)]
    node[p] = 0
    node[pu] = 1
    cnt = [0,0]
    for i in range(2):
        if i == 0:
            q.append(p)
        else:
            q.append(pu)
        while q:
            u = q.pop()
            for v in root[u]:
                if node[v] < 0:
                    node[v] = i
                    q.append(v)
                    cnt[i] += 1
    if cnt[0] > cnt[1]:
        print('Fennec')
    else:
        print('Snuke')

if __name__ == '__main__':
    main()