s = input()
ans = "NO"
if s[:7] == "keyence" or s[-7:] == "keyence": ans = "YES"
elif len(s) >= 7:
    k = "keyence"
    for i in range(len(s)):
        if k[i] == s[i]: continue
        else: break
    if s[:i]+s[-(7-i):] == "keyence": ans = "YES"
print(ans)