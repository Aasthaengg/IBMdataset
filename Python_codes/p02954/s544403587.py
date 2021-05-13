s = input()
n = len(s)
l = [0]
for i in range(n - 1):
    if s[i] != s[i + 1]:
        l.append(i + 1)
l.append(n)
ans = [0] * n
for i in range(1, len(l) - 1, 2):
    p = l[i] - l[i - 1]
    q = l[i + 1] - l[i]
    ans[l[i] - 1] = (p + 1) // 2 + q // 2
    ans[l[i]] = p // 2 + (q + 1) // 2
print(' '.join(map(str, ans)))
