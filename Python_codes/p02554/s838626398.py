n = int(input())
mod = 10**9+7
print((((10**n)%mod)-(9**n%mod)-(9**n%mod)+(8**n%mod))%mod)