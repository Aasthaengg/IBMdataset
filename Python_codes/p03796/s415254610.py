n = int(input())
mod = 10**9 + 7

pow = 1
for i in range(n):
    pow = pow*(i+1)%mod

print(pow)
