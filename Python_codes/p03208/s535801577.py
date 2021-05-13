INF = float("inf")

N,K = map(int,input().split())
h = [int(input()) for i in range(N)]
h.sort()

ans = INF
for i in range(0,N-K+1,1):
    ans = min(ans,h[i+K-1]-h[i])
print(ans)