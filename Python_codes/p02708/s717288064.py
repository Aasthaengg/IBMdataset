n, k = map(int, input().split())

n = n+1
mod = 10**9+7

ans = 0
for i in range(k, n+1):
    m1 = ((i+1)*i//2)
    m2 = ((n-i+1+n)*i//2)

    ans = (ans + m2 - m1 + 1) % mod

print(ans)
