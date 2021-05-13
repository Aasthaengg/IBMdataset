N = int(input())
A = list(map(int, input().split()))

mod = 10**9+7

cnt = [0]*60
bt = [0]*60

for a in A:
    for i in range(60):
        cnt[i] += (a>>i)&1

ans = 0
for i in range(60):
    x = cnt[i]
    y = x*(N-x)%mod
    ans += y*2**i
    ans %= mod

print(ans)