import sys
sys.setrecursionlimit(500000)

N,K = map(int,input().split())
T = [[]*N for i in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    T[a-1].append(b-1)
    T[b-1].append(a-1)
visited = [0]*N
ans = 1
def bfs(i,bb,b):
    global ans
    visited[i] = 1
    ans = (ans*(K-bb-b))%(10**9+7)
    cnt = 0
    for j in T[i]:
        if visited[j] == 1:
            continue
        bfs(j,b+cnt,1)
        cnt += 1
bfs(0,0,0)
print(ans)


