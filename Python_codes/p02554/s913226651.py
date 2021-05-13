mod = 10**9+7
N = int(input())
ans = (pow(10,N,mod) - 2*pow(9, N, mod) + pow(8, N, mod))%mod
if ans < 0:
    ans += mod
print(ans)
