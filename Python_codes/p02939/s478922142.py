s = input()

ans = 1
tmp = s[0]
t = False

for i in range(1, len(s)):
    if t:
        tmp = s[i - 1] + s[i]
        t = False
        ans += 1
        continue
        
    if tmp == s[i]:
        t = True
        
    else:
        ans += 1
        tmp = s[i]

print(ans)