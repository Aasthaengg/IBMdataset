n = int(input())
mod = 10**9+7
print((10**n-9**n-9**n+8**n)%mod if n >= 2 else 0)