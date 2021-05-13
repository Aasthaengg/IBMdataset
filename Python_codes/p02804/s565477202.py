n, k = map(int, input().split())
a = list(map(int, input().split()))
mod = int(1e+9 + 7)
a = sorted(a)

kai = [1]*(n+1)
gyaku = [1]*(n+1)

for i in range(2, n+1):
    kai[i] = kai[i-1]*i % mod
    gyaku[i] = gyaku[i-1]*pow(i, mod-2, mod) %mod

answer = 0
for i in range(k-1,n):
    answer = (answer + a[i] * kai[i] * gyaku[(i)-(k-1)] * gyaku[k-1]) % mod

answer2 = 0
for i in range(n-k+1):
    answer2 = (answer2 + a[i] * kai[n-i-1] * gyaku[(n-i)-k] * gyaku[k-1]) % mod


if k == 1:
    print(0)
else:
    print((answer - answer2)%mod)
