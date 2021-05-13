N = int(input())
MOD = 10**9 + 7
ans = 1
for k in range(1,N+1):
    ans *= k
    ans %= MOD
print(ans)
