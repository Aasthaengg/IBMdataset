n,k = map(int, input().split())
r = n //k
n -= k*r
ans = min(n, abs(n-k))
print(ans)