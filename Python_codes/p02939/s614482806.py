s=input()
ans = 1
pre = s[0]
now = ''
for i in range(1,len(s)):
    now += s[i]
    if pre == now:
        pass
    else:
        ans += 1
        pre = now
        now = ''
print(ans)