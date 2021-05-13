s = str(input())
t = str(input())
cnt = 0
for i in range(len(s)):
    if s[i]!=t[i]:
        cnt = cnt + 1
    else:
        continue
print(cnt)