li_s = list(input())
k = int(input())
z = ord('z')
ans = ''
for i in range(len(li_s)):
    if i < len(li_s) - 1 and li_s[i] == 'a':
        ans += 'a'
    elif i < len(li_s)-1 and k-(z-ord(li_s[i])+1) >= 0:
        k -= z-ord(li_s[i])+1
        ans = ans + 'a'
    elif i < len(li_s)-1:
        ans = ans + li_s[i]
    elif i == len(li_s) - 1:
        p = ord(li_s[i])  + k
        p %= 26
        p += 78
        if 97 <= p:
            ans = ans + chr(p)
        else:
            ans = ans + chr(p+26)
print(ans)