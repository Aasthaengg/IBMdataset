s = input()
tmp = s[0]
ans = 0
x = ''
for i in range(1,len(s)):
    if tmp==x+s[i]:
        x = s[i]
    else:
        tmp = x+s[i]
        x = ''
        ans += 1
print(ans+1)