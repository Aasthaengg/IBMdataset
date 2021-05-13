N = int(input())
a = [int(x) for x in input().split()]
mod = 10**9+7
#最小公倍数を割った商の和を求める
import fractions
lcm = a[0]
for i in range(1,N):
    lcm = lcm * a[i] // fractions.gcd(lcm,a[i])
ans = 0
for i in range(N):
    ans += lcm//a[i]
print(ans%mod)