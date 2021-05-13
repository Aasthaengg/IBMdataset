N = int(input())
A = list(map(int,input().split()))
import fractions
mod = 10**9+7
lcm = A[0]
for i in range(1,N):
    lcm = lcm*A[i]//fractions.gcd(lcm,A[i])
ans = 0
for i in range(N):
    ans += lcm*pow(A[i],mod-2,mod)
print(ans%mod)