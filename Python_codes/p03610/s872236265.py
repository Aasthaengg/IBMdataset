s = input()

ans = ""
for i in range(len(s)):
    if i % 2 == 1:
        continue
    else:
        ans+=s[i]

print(ans)