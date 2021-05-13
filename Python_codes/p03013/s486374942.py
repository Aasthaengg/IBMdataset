mod = 1000000007

n, m = map(int, input().split())
s = [0] * (n + 2)
for _ in range(m):
    a = int(input())
    s[a] = -1

s[0] = 1
for i in range(0, n):
    if s[i] < 0:
        continue
    if s[i + 1] >= 0:
        s[i + 1] = (s[i + 1] + s[i]) % mod
    if s[i + 2] >= 0:
        s[i + 2] = (s[i + 2] + s[i]) % mod

print (s[n])
