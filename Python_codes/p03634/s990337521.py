import queue
import sys
sys.setrecursionlimit(10**7)
n = int(input())

abc = [[] for i in range(n+1)]

for i in range(n-1):
    a,b,c = map(int,input().split())
    abc[a].append([b,c])
    abc[b].append([a,c])

Q,k = map(int,input().split())
xy = [[int(i) for i in input().split()] for j in range(Q)]

q = queue.Queue()

q.put(k)

path = [-1]*(n+1)
path[k] = 0

def dfs(p):
    for i in range(len(abc[p])):
        num = abc[p][i][0]
        if path[num] != -1:
            continue
        else:
            path[num] = path[p] + abc[p][i][1]
            dfs(num)

dfs(k)

for i in range(Q):
    print(path[xy[i][0]]+path[xy[i][1]])