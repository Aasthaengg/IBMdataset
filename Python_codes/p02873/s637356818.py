s = input()
n = len(s)
ans = 0
l = 0
ll = [0] * (n + 1)
r = 0
rl = [0] * (n + 1)
for i in range(n):
    if s[i] == '<':
        l += 1
        ll[i+1] = l
    else:
        l = 0
    if s[n-1-i] == '>':
        r += 1
        rl[n-i-1] = r
    else:
        r = 0
for i in range(n + 1):
    ans += max(rl[i], ll[i])
print(ans)