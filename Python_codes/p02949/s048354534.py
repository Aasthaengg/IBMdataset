#負閉路あり最短経路(逆符号最長)
#aoj,grl1b
import sys
n,m,p = map(int, input().split( ))
E = [[] for _ in range(n)]
inf = 10**12
for _ in range(m):
    a,b,c = map(int, input().split( ))
    E[a-1].append([b-1,p-c])###


D = [inf for _ in range(n)]
D[0] = 0
for _ in range(n):
    for ve in range(n):
        for ed in E[ve]:
            D[ed[0]] = min(D[ed[0]], D[ve] + ed[1])
#上終わってから更新あったら負閉路
#print(*D)
for _ in range(n+10):
    for ve in range(n):
        for ed in E[ve]:
            if D[ed[0]] > D[ve] + ed[1] and D[ed[0]]<inf//10:##後半の条件は始点から到達できる、の意味
                #print(D[ed[0]], D[ve], ed[1])
                D[ed[0]] = -inf

"""
for i in range(n):
    if E[i]:
        for ed in E[i]:
            if D[i] + ed[1] < D[ed[0]] and D[ed[0]]<inf//10:
                print(-1)
                sys.exit()
"""
#print(*D)
if D[n-1]>-inf//10:
    print(max(0,-D[n-1]))
else:
    print(-1)