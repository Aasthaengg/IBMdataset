MOD = 2019
s = list(input())
s.reverse()
n = len(s)
lis = [0] * 2020
ans = 0
x = 1
tot = 0
for i in range(n):
    lis[tot] += 1
    tot += int(s[i]) * x
    tot %= MOD
    ans += lis[tot]
    x *= 10
    x %= MOD
print(ans)
