d = {}
for i in range(26):
    d[i] = 0
s = input()
n = len(s)
for i in range(n):
    x = s[i]
    y = ord(x) - 97
    d[y] += 1
ans = 0
for i in range(26):
    ans += d[i]*(n-d[i])
ans = ans // 2 + 1
print(ans)