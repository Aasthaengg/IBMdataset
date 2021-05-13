# https://atcoder.jp/contests/abc138/tasks/abc138_d
import sys
sys.setrecursionlimit(2*2*10**5)

def dfs(i,p,edges,num):
    
    for j in edges[i]:
        if(j!=p):
            
            num[j] += num[i]
            
            dfs(j,i,edges,num)
    
def input():
    return sys.stdin.readline()[:-1]

N,Q = map(int,input().split())


#隣接リスト
edges = [ [] for i in range(N)]
num = [0]*N


for i in range(N-1):
    a0,b0 = map(int,input().split())

    edges[a0-1].append(b0-1)
    edges[b0-1].append(a0-1)
    
for i in range(Q):
    p0,x0 = map(int,input().split())

    num[p0-1] += x0
    
dfs(0,-1, edges, num)
    
for i in range(N):
    print(num[i], end=" ")
