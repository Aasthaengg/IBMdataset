def sigma(n):
    return n * (n + 1) // 2

s = list(map(lambda x : 1 if x == '<' else -1, input()))
l = [s[0]]
for c in s[1:]:
    if c * l[-1] > 0:
        l[-1] += c
    else:
        l.append(c)
ans = 0
now = 0
for c in l:
    if c < 0:
        ans -= min(now, abs(c))
    ans += sigma(abs(c))
    now = abs(c)
print(ans)