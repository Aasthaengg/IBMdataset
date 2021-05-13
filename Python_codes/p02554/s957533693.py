N = int(input())
mod = 10**9+7
S = 10**N%mod
O = 8**N%mod

ans = ((S +O)%mod - 2*9**N%mod)%mod
print(ans)