n,k = map(int,input().split())
mod = 7+10**9

a = [0]*(k+1)

for i in reversed(range(1,k+1)):
    a[i] += pow(k//i, n, mod)
    for j in range(2,k//i+1):
        a[i] -= a[i*j]

ans = 0
for i in range(1,k+1):
    ans += (i*a[i]) % mod

print(ans % mod)