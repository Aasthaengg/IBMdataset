INF=float("inf")
N=int(input())
a=list(map(int, input().split()))
cum = [0]*(N+1)
for i in range(1, N+1):
    cum[i] = cum[i-1] + a[i-1]
s = sum(a)
ans = INF
for i in range(1, N):
    ans = min(ans, abs(cum[i] - (s - cum[i])))
print(ans)