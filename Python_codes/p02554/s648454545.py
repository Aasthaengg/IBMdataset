N = int(input())
MOD = 7+10**9
ans = (10**N)%MOD
ans = (ans + ((8**N)%MOD))%MOD
ans = (ans - ((2*(9**N))%MOD))%MOD
ans = (ans+MOD)%MOD
print(ans)