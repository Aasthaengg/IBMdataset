n = int(input())
s = list(map(int, input().split()))
mod = 10**9 + 7
m = len(bin(max(s))) - 2
p = [0] * m
q = [0] * m

for i in s:
    for j in range(m):
        if (i >> j) & 1 == 1:
            p[j] += 1
        else:
            q[j] += 1

res = 0
r = 1
for k in range(m):
    res += p[k] * q[k] % mod * r
    res %= mod
    r = r * 2 % mod
print(res)
