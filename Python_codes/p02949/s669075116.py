
"""

https://atcoder.jp/contests/abc137/tasks/abc137_e

辺の重みからPを引いておく
→あとはベルマンフォード？

正の閉路探索→むずくね？
閉路があったとしても、増えなきゃあっていい…

→まずゴールにたどり着ける頂点を列挙
→たどり着けない点は無意味なのでremove

→あとはベルマンフォード
"""

import sys
sys.setrecursionlimit(200000)

N,M,P = map(int,input().split())

lis = [ [] for i in range(N) ]
rev = [ [] for i in range(N) ]
exist = [False] * N

for i in range(M):

    A,B,C = map(int,input().split())
    A -= 1
    B -= 1

    lis[A].append([B , C - P])
    rev[B].append(A)

def dfs(v):

    exist[v] = True
    for nex in rev[v]:
        if not exist[nex]:
            dfs(nex)

dfs(N-1)

dis = [float("-inf")] * N
dis[0] = 0

for i in range(N+1):

    flag = False

    for v in range(N):
        for uc in lis[v]:

            if exist[uc[0]] and dis[uc[0]] < dis[v] + uc[1]:
                #print (uc[0] , dis[v] + uc[1])
                dis[uc[0]] = dis[v] + uc[1]
                flag = True

if flag:
    print (-1)
else:
    print (max( 0 , dis[N-1] ))
