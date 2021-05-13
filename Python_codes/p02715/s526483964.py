#メモ化再帰以外は実装が厳しい

n,k = map(int, input().split( ))
memo = [-1]*(k+1)
mod = 10**9+7
def rec(x):
    if memo[x]>=0:
        return memo[x]
    mult = 0
    for i in range(x*2,k+1,x):
        mult += rec(i)
    res = memo[x] = pow(k//x,n,mod) - mult
    return res
ans = 0
rec(1)
for i in range(1,k+1):
    ans += i*memo[i]
print(ans%mod)
  
