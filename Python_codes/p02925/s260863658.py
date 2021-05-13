N = int(input())
A = [list(map(lambda x:int(x)-1, input().split())) for _ in range(N)]

M = N*N

def c(a,b):
    if a>b: a,b=b,a
    return a*N+b

G = [[] for _ in range(M)]
for i in range(N):
    a = A[i]
    x = i
    for j in range(N-1-1):
        y1 = a[j]
        y2 = a[j+1]
        G[c(x,y1)].append(c(x,y2))

dp = [0]*M
started = [False]*M
finished = [False]*M
for i in range(N):
    for j in range(i+1, N):
        s = c(i,j)
        if started[s]: continue
        stk = [(s, 0)]
        while stk:
            v, s = stk.pop()
            if s == 0:
                if started[v]:
                    if not finished[v]:
                        print(-1)
                        exit()
                    continue
                started[v] = True
                stk.append((v, 1))
                for to in G[v]:
                    stk.append((to, 0))
            else:
                finished[v] = True
                for to in G[v]:
                    dp[v] = max(dp[v], dp[to] + 1)

print(max(dp) + 1)