s = input()
ans = 10 ** 9
for alpha in range(97,123):
    a = chr(alpha)
    cnt = 0
    ret = 0
    for i in range(len(s)):
        if s[i] == a:
            ret = max(ret,cnt)
            cnt = 0
        else:
            cnt += 1
    ret = max(ret,cnt)
    ans = min(ans,ret)
print(ans)
