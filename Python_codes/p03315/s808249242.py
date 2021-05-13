s = str(input())
ans=0
for x in range(len(s)):
    if s[x] == '+':
        ans += 1
    else:
        ans -= 1

print(ans)
