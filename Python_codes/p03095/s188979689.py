n = int(input())
s = list(input())
mod = 10**9+7
alp = [0] * 26

for i in range(n):
    alp[ord(s[i]) - ord("a")] += 1

ans = 1
for c in alp:
    if (c != 0):
        ans *= (c+1)

print((ans - 1) % mod)
