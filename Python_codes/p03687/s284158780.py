S = input()
ans = len(S)
for i in range(26):
    s = chr(97+i)
    tmp = -1
    res = 0
    flg = False
    for j in range(len(S)):
        if S[j] == s:
            flg = True
            res = max(res, j-tmp-1)
            tmp = j
    if not flg:
        continue
    ans = min(ans, max(res, len(S)-tmp-1))
print(ans)

