s= input()

now = s[0]
ans = 0
flg = 0
for i in range(1,len(s)):
    if flg == 0:
        if now == s[i]:
            pass
        elif now != s[i]:
            ans += 1
            flg = 1
            now = s[i]

    else:
        if now == s[i]:
            pass
        elif now != s[i]:
            ans += 1
            flg = 0
            now = s[i]
            
print(ans)