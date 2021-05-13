s = str(input())
color = s[0]
cnt = 0
for i in range(1,len(s)):
    if color != s[i]:
        color = s[i]
        cnt += 1
print(cnt)