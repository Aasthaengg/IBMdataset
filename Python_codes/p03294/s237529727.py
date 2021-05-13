import fractions
N = int(input())
a = list(map(int, input().split()))
res = a[0]
for i in range(1,N):
    res = res*a[i]//fractions.gcd(res,a[i])
res -= 1
ans = 0
for i in range(N):
    ans += res%a[i]
print(ans)