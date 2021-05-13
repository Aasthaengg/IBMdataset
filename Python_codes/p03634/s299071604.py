N=int(input())
import sys
sys.setrecursionlimit(10**6)
T=[[] for _ in range(N)]
for i in range(N-1):
    a,b,c=map(int, input().split())
    T[a-1].append((b-1,c))
    T[b-1].append((a-1,c))

Q,K=map(int, input().split())
D=[-1]*N
D[K-1]=0
def dfs(start, nowd):
    to=T[start]
    for t in to:
        next_node,c=t
        if D[next_node]!=-1:
            continue
        nextd=nowd+c
        D[next_node]=nextd
        dfs(next_node, nextd)
dfs(K-1,0)
# print(D)
for i in range(Q):
    x,y=map(int, input().split())
    print(D[x-1]+D[y-1])
