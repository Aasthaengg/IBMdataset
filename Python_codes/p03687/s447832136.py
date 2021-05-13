S = input()
n = len(S)
ans = 1e100
for i in range(26):
    t = chr(ord('a') + i)
    if t not in S:continue
    tmp = 0
    cnt = 0
    for s in S + t:
        if s == t:
            tmp = max(tmp, cnt)
            cnt = 0
        else:
            cnt += 1
    ans = min(ans, tmp)
print(ans)
