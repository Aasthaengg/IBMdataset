s = input()
n = len(s)
mod = 2019

cum = [0]*n
cum[n-1] = int(s[-1]) % mod
d = [1]*n
for i in range(n-1)[::-1]:
    d[i] = d[i+1]*10%mod

for i in range(0, n-1)[::-1]:
    a = int(s[i]) * d[i] % mod
    cum[i] = (cum[i+1]+a) % mod
cnt = [0]*mod

ans = 0
for i in cum[::-1]:
    ans += cnt[i]
    cnt[i] += 1
    if i == 0:
        ans += 1
print(ans)