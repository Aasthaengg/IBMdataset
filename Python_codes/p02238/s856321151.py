import sys
sys.setrecursionlimit(10**7)
time = 0
def input():
    return sys.stdin.readline()
n = int(input())
G = [[]]
d = [0]*(n+1)
f = [0]*(n+1)
for _ in range(n):
    G.append(list(map(int,input().split()))[2:])
def dfs(e):
    global time
    d[e] = time
    for nexte in G[e]:
        if d[nexte] == 0:
            time += 1
            dfs(nexte)
    time += 1
    f[e] = time

for i in range(1,n+1):
    if d[i] == 0:
        time += 1
        dfs(i)
for i in range(1,n+1):
    print(i,d[i],f[i])

