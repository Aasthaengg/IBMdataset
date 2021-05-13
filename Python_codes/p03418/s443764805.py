N,K = map(int,input().split())

ans = 0
for b in range(K+1,N+1):
    m = N//b
    r = N%b
    ans += max(r-K+1,0)+m*(b-K)

if K == 0:
    ans = N**2

print(ans)