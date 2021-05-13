s = str(input())

ans = ""
for i in range(len(s)):
    if i % 2 != 0:
        continue
    else:
        ans += s[i]

print(ans)