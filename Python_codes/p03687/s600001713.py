S = input()

ans = 1e9
for c in range(ord('a'), ord('a') + 26):
    c = chr(c)
    res = []
    for i, s in enumerate(S):
        if c == s:
            res.append(i)
    if len(res) == 0:
        continue
    if len(res) > 1:
        D = [res[i + 1] - res[i] - 1 for i in range(0, len(res) - 1)]
        res1 = max(D)
    else:
        res1 = 0
    res2 = max(res[0], len(S) - res[-1] - 1)
    ans = min(ans, max(res1, res2))

print(ans)
